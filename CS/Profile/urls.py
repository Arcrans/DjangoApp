from django.urls import path, re_path
from django.conf.urls import include, url
from django.contrib.auth.models import User
from Profile import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Profile')
# from rest_framework import routers, serilizers, viewsets

urlpatterns = [
    url(r'Perfil/', schema_view),
    re_path(r'profileList/$', views.profileMethods.as_view()),
    re_path(r'ciudadList/$', views.ciudadMethods.as_view()),
    re_path(r'generoList/$', views.generoMethods.as_view()),
    re_path(r'ocupacionList/$', views.ocupacionMethods.as_view()),
    re_path(r'estadoList/$', views.estadoMethods.as_view()),
    re_path(r'estadoCivilList/$', views.estadoCivilMethods.as_view()),
]