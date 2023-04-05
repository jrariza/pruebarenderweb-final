from django.db import models

# Create your models here.

class Genere(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    
class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    name = models.CharField(max_length=50)
    sinopsys = models.CharField(max_length=200)
    genere = models.ForeignKey(Genere, on_delete=models.DO_NOTHING)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    
class Autor(models.Model):
    name = models.CharField(max_length=50)
    surnames = models.CharField(max_length=100)
    born_date = models.DateField()
    born_country = models.CharField(max_length=50)
    
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    
class Publishing(models.Model):
    release_date = models.DateField()
    author = models.ForeignKey(Autor, on_delete=models.DO_NOTHING)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)