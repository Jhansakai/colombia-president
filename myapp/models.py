from django.db import models

# Create your models here.
class Partido(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
       return "{}".format(self.name)


class Presidente(models.Model):
    numero = models.IntegerField()
    name = models.CharField(max_length=60)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    inicio = models.IntegerField()
    final = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
       return "{}".format(self.name)
    
