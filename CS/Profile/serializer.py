from rest_framework import routers, serializers, viewsets

from Profile.models import profileModel
from Profile.models import ciudadModel
from Profile.models import generoModel
from Profile.models import ocupacionModel
from Profile.models import estadoModel
from Profile.models import estadoCivilModel


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profileModel
        fields = ('__all__')


class ciudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudadModel
        fields = ('__all__')


class generoSerializer(serializers.ModelSerializer):
    class Meta:
        model = generoModel
        fields = ('__all__')


class ocupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ocupacionModel
        fields = ('__all__')


class estadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = estadoModel
        fields = ('__all__')


class estadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = estadoCivilModel
        fields = ('__all__')
