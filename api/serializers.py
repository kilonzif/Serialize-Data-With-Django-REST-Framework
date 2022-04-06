from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    
    class Meta:
        model = User
        exclude = ("last_login", "is_superuser", "is_staff", "is_active", "date_joined", "user_permissions", "groups")

class StudentSerializer(serializers.ModelSerializer):
    account = UserSerializer()
    class Meta:
        model = Student
        fields = '__all__'
        
    def create(self, validated_data):
        user_data = validated_data.pop('account')
        print(user_data)
        user = User.objects.create(**user_data)
        student = Student.objects.create(account=user, **validated_data)
        return student
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('account')
        account = instance.account

        instance.gender = validated_data.get('gender', instance.gender)
        instance.location = validated_data.get('location', instance.location)
        instance.stack = validated_data.get('stack', instance.stack)
        instance.save()

        account.username = user_data.get('username', account.username)
        
        account.first_name = user_data.get(
            'first_name',
            account.first_name
        )
        
        account.last_name = user_data.get(
            'last_name',
            account.last_name
        )
        
        account.email = user_data.get(
            'email',
            account.email
        )
        
        account.password = user_data.get(
            'password',
            account.password
        )

        account.save()

        return instance


class ClassroomSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Classroom
        fields = '__all__'
        
    def create(self, validated_data):
        from django.db import transaction
        
        with transaction.atomic():
            student_data = validated_data.pop("student")
            data = student_data['account']
            
            email = data["email"]
            username = data["username"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            password = make_password(data["password"])
            
            account = User.objects.create(username=username, first_name=first_name, last_name=last_name, 
                                          email=email, password=password)
            
            avatar = student_data["avatar"]
            gender = student_data["gender"]
            location = student_data["location"]
            stack = student_data["stack"]
            
            student = Student.objects.create(account=account, avatar=avatar, gender=gender, 
                                                 location=location, stack=stack)
            classroom = Classroom.objects.create(student=student, **validated_data)
            
        return classroom
    
    def update(self, instance, validated_data):
        student_data = validated_data.pop('student')
        account_data = student_data["account"]
        account = instance.student.account
        student = instance.student

        instance.classroom = validated_data.get('classroom', instance.classroom)
        instance.mentor = validated_data.get('mentor', instance.mentor)
        instance.save()
        
        student.avatar = student_data.get('avatar', student.gender)
        student.gender = student_data.get('gender', student.gender)
        student.location = student_data.get('location', student.location)
        student.stack = student_data.get('stack', student.stack)
        student.save()

        account.username = account_data.get('username', account.username)
        
        account.first_name = account_data.get('first_name', account.first_name)
        
        account.last_name = account_data.get(
            'last_name',
            account.last_name
        )
        
        account.email = account_data.get(
            'email',
            account.email
        )
        
        account.password = make_password(account_data.get(
            'password',
            account.password
        ))

        account.save()

        return instance