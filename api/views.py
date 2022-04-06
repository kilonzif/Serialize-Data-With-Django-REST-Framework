from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .permissions import *

def index(request):
    return render(request, 'index.html')

class AllStudents(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, uuid=None):
        if uuid:
            student = Student.objects.get(uuid=uuid)
            serializer = StudentSerializer(student)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)   

    def put(self, request, uuid=None):
        student = Student.objects.get(uuid=uuid)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, uuid=None):
        student = get_object_or_404(Student, uuid=uuid)
        student.delete()
        return Response({"status": "success", "data": "student Deleted"})
    

class MyUsers(APIView):
    def get(self, request, pk=None):
        if pk:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
        
class ClassroomData(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    
    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, pk=None):
        if pk:
            classroom = Classroom.objects.get(id=pk)
            serializer = ClassroomSerializer(classroom)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)   

    def put(self, request, pk=None):
        classroom = Classroom.objects.get(id=pk)
        serializer = ClassroomSerializer(classroom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, uuid=None):
        classroom = get_object_or_404(Classroom, id=id)
        classroom.delete()
        return Response({"status": "success", "data": "student Deleted"})       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        