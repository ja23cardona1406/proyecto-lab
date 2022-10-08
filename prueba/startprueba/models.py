from django.db import models


# Create your models here.

class Usuario(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')                
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre usuario')
    apellido = models.CharField(max_length = 50, verbose_name = 'Apellido usuario')
    nombreDeUsuario = models.CharField(max_length = 50, verbose_name = 'Nombre de usuario')

