from django.db import models
from django.utils import timezone



class Mymodel(models.Model):
    id = models.AutoField(primary_key=True)
    odd = models.DecimalField(default = 0.0, max_digits=7, decimal_places=2)
    hora_criacao = models.DateTimeField(default = timezone.now)
    apostadores = models.IntegerField()
    
