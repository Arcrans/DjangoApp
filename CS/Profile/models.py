from django.db import models

# Create your models here.

from django.utils import timezone


class estadoCivilModel(models.Model):
    nombre = models.CharField(max_length=254, null= False)

    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default= timezone.now)
    

    def __str__(self):
        return self.nombre



class estadoModel (models.Model):
    nombre = models.CharField(max_length=254, null= False)
    
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default= timezone.now)
    def __str__(self):
        return self.nombre

class ocupacionModel(models.Model):
    nombre = models.CharField(max_length=254, null= False)

    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default= timezone.now)
    

    def __str__(self):
        return self.nombre
     
class generoModel(models.Model):
    nombre = models.CharField(max_length=254, null= False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.nombre
     
class ciudadModel(models.Model):
  
    nombre = models.CharField(max_length=254, null= False)

    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default= timezone.now)
    
    def __str__(self):
        return self.nombre

class profileModel(models.Model):
   
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default= timezone.now)
    
    nombre = models.CharField(max_length=254, null= False)
    apellidoPaterno = models.CharField(max_length=254, null= False)
    apellidoMaterno = models.CharField(max_length=254, null= False)
    edad = models.IntegerField(null=False)

    ciudad = models.ForeignKey(ciudadModel,on_delete = models.CASCADE)
    genero = models.ForeignKey(generoModel,on_delete = models.CASCADE)
    ocupacion = models.ForeignKey(ocupacionModel,on_delete = models.CASCADE)
    estado = models.ForeignKey(estadoModel,on_delete = models.CASCADE)
    estadoCivil = models.ForeignKey(estadoCivilModel,on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre, self.apellidoPaterno, self.apellidoMaterno, self.edad

    class Meta:
        db_table = 'Profile'

