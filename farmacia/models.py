from django.db import models

class Marca(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    
    def __str__(self):
       return "{}".format(self.name)

class Vitaminas(models.Model):
    name = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    lote = models.IntegerField()
    fecha_vencimiento = models.IntegerField()
    
    def __str__(self):
       return "{}".format(self.name)

class Analgesicos(models.Model):
    name = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    lote = models.IntegerField()
    fecha_vencimiento = models.IntegerField()
    
    def __str__(self):
       return "{}".format(self.name)
    
class Antibiotico(models.Model):
    name = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    lote = models.IntegerField()
    fecha_vencimiento = models.IntegerField()
    
    def __str__(self):
       return "{}".format(self.name)    
    
class Antivirales(models.Model):
    name = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    lote = models.IntegerField()
    fecha_vencimiento = models.IntegerField()
    
    def __str__(self):
       return "{}".format(self.name)    

