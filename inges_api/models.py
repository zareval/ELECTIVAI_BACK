from django.db import models

# Create your models here.
class persona(models.Model):
    nombre=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=50)
    f_nacimiento=models.DateField()
    biografia=models.CharField(max_length=500)


class pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    duracion = models.IntegerField()
    pais = models.CharField(max_length=50)
    f_estreno = models.DateField()
    trailer = models.URLField(max_length=200)
    e_produccion = models.URLField(max_length=100)
    poster = models.URLField(max_length=100) 
    director = models.CharField(max_length=500)
    protagonistas = models.ManyToManyField(persona) 


class serie(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    duracion = models.IntegerField()
    pais = models.CharField(max_length=50)
    f_estreno = models.DateField()
    trailer = models.URLField(max_length=200)
    e_produccion = models.URLField(max_length=100)
    poster = models.URLField(max_length=100) 
    director = models.CharField(max_length=500)
    protagonistas = models.ManyToManyField(persona)  


    '''
    De muchos a muchos y forenkey , un director puede dirigir una pelicula y una pelicula puede tener un director,
    en el otro un protagonista puede actuar en muchas peliculas y una pelicula puede tener muchos directores.
    '''
