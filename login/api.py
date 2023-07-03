from django.urls import path
from user.views import  *

urls = [
    path('user/signup/',Signup),
    path('user/signin/',SignIn),
]



