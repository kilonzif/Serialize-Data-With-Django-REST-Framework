from statistics import mode
import uuid
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

GENDER = (
    ('Male','MALE'),
    ('Female','FEMALE'),
    ('Other','OTHER'),
)

TYPES =(    
    ('Python', 'PYTHON'),
    ('Java', 'JAVA'), 
)

class Student(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = CloudinaryField('image', blank=True, null=True)
    gender = gender = models.CharField(choices=GENDER, max_length=55)
    location = models.CharField(max_length=55)
    joined_on = models.DateTimeField(auto_now_add=True)
    stack = models.CharField(choices=TYPES, max_length=55)
    
    def __str__(self):
        return self.account.username
    
class Classroom(models.Model):
    student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE, related_name='student_details')
    classroom = models.CharField(blank=True, null=True, max_length=85)
    mentor = models.CharField(blank=True, null=True, max_length=85)
    
    def __str__(self):
        return self.classroom
    
    
        