from django.db import models

 

# Create your models here.

class Maquina(models.Model):
   idMaquina = models.IntegerField(primary_key=True,verbose_name='Id de maquina')
   marcaMaquina = models.CharField(max_length=45,verbose_name='Nombre de la marca')
   modeloMaquina = models.CharField(max_length=45,verbose_name='Modelo de la maquina')

   def __str__(self):
       return self.marcaMaquina
