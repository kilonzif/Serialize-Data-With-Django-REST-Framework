from .views import *
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('', views.index, name='index'),
    path('students', AllStudents.as_view()),
    path('students/<str:uuid>', AllStudents.as_view()),
    path('users', MyUsers.as_view()),
    path('users/<int:pk>', MyUsers.as_view()),
    path('classrooms', ClassroomData.as_view()),
    path('classrooms/<int:pk>', ClassroomData.as_view()),
    path('api/token-auth', obtain_auth_token)
]