
from pickle import TRUE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser

class User(AbstractBaseUser):
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.first_name


class publisher(models.Model):
    name = models.CharField(max_length=50)
    id= models.CharField(max_length=50,primary_key=TRUE)
   
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100,blank=True)
    isbn = models.CharField(max_length=100,blank=True)
    price =models.IntegerField()
    edition =models.CharField(max_length=100,blank=True)
    authno=models.CharField(max_length=100,blank=True)
    authors = models.ManyToManyField(Author)
    cetegory = (
        ('t', 'tech'),
        ('n', 'non tech'), 
    )
    cetegory = models.CharField(max_length=1, choices=cetegory)
    publisher=models.ForeignKey(publisher,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class reader(models.Model):
    name= models.CharField(max_length=100,blank=True)
    email=models.CharField(max_length=100,blank=True)
    Book=models.ManyToManyField(Book)









    


 