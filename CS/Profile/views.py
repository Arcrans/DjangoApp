from django.shortcuts import get_object_or_404

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from Profile.models import profileModel
from Profile.models import ciudadModel
from Profile.models import generoModel
from Profile.models import ocupacionModel
from Profile.models import estadoModel
from Profile.models import estadoCivilModel

from Profile.serializer import profileSerializer
from Profile.serializer import ciudadSerializer
from Profile.serializer import generoSerializer
from Profile.serializer import ocupacionSerializer
from Profile.serializer import estadoSerializer
from Profile.serializer import estadoCivilSerializer

import coreapi
from rest_framework.schemas import AutoSchema


class estadoCivilSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields=[]
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('nombre'),      
            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class estadoSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields=[]
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('nombre'),      
            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class ocupacionSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields=[]
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('nombre'),      
            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class generoSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields=[]
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('nombre'),      
            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class ciudadSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields=[]
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('nombre'),      
            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class profileSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields=[]
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('nombre'),
                coreapi.Field('apellidoPaterno'),
                coreapi.Field('apellidoMaterno'),
                coreapi.Field('edad'),
                coreapi.Field('ciudad'),      
                coreapi.Field('genero'),
                coreapi.Field('ocupacion'),
                coreapi.Field('estado'),
                coreapi.Field('estadoCivil')
            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields


class profileMethods(APIView):
    schema = profileSchema()
    def get(self, request, format=None):
        print("Metodo profile")
        queryset = profileModel.objects.filter(delete = False)
        serializer = profileSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self,request, format=None):
        serializer = profileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ciudadMethods(APIView):
    schema = ciudadSchema()

    def get(self, request, format=None):
        print("Metodo ciudad")
        queryset = ciudadModel.objects.filter(delete = False)
        serializer = ciudadSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self,request, format=None):
        serializer = ciudadSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class generoMethods(APIView):
    schema = generoSchema()

    def get(self, request, format=None):
        print("Metodo genero")
        queryset = generoModel.objects.filter(delete = False)
        serializer = generoSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self,request, format=None):
        serializer = generoSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ocupacionMethods(APIView):
    schema = ocupacionSchema()

    def get(self, request, format=None):
        print("Metodo ocupacion")
        queryset = ocupacionModel.objects.filter(delete = False)
        serializer = ocupacionSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self,request, format=None):
        serializer = ocupacionSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class estadoMethods(APIView):
    schema = estadoSchema()

    def get(self, request, format=None):
        print("Metodo estado")
        queryset = estadoModel.objects.filter(delete = False)
        serializer = estadoSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self,request, format=None):
        serializer = estadoSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class estadoCivilMethods(APIView):
    schema = estadoCivilSchema()

    def get(self, request, format=None):
        print("Metodo estado civil")
        queryset = estadoCivilModel.objects.filter(delete = False)
        serializer = estadoCivilSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self,request, format=None):
        serializer = estadoCivilSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#________________ SCHEMAS ____________________





