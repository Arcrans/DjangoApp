from django.shortcuts import get_object_or_404

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from Login.models import Example2
from Login.serializer import Example2Serializers


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.conf.urls import url

import coreapi
from rest_framework.schemas import AutoSchema

class ExampleList2Schema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields=[]
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('name'),
                coreapi.Field('year')
            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class ExampleList2(APIView):
    schema = ExampleList2Schema()
    def get(self, request,):
        print("Metodo get filter")
        queryset = Example2.objects.filter(delete = False)
        serializer = Example2Serializers(queryset, many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer = Example2Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Create your views here.


class CustonAuthToken(ObtainAuthToken):

    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data,
            context = {
            'request': request,
            }
        )                                     
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
        'token': token.key,
        'user_id': user.pk,
        'username': user.username
        }) 

