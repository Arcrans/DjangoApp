from django.urls import path, re_path
from django.conf.urls import include, url
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from Login.views import CustonAuthToken

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Login')
from Login import views

# from rest_framework import routers, serilizers, viewsets

urlpatterns = [
    url(r'Login', schema_view),
    re_path(r'Login/$', CustonAuthToken.as_view()),
    re_path(r'example_list2/$', views.ExampleList2.as_view()),
]