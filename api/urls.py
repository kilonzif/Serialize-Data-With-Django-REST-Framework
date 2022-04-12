from .views import *
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns=[
    path('', views.index, name='index'),
    path('students', AllStudents.as_view()),
    path('students/<str:uuid>', AllStudents.as_view()),
    path('users', MyUsers.as_view()),
    path('users/<int:pk>', MyUsers.as_view()),
    path('classrooms', ClassroomData.as_view()),
    path('classrooms/<int:pk>', ClassroomData.as_view()),
    path('api/token-auth', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]