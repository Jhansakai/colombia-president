from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=60)
    descripcion = models.TextField()
    
    def __str__(self):
       return "{}".format(self.name)

class Producto(models.Model):
    name = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    lote = models.IntegerField()
    fecha_vencimiento = models.IntegerField()
    descripcion =  models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
       return "{}".format(self.name)
