from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentname = models.CharField(max_length=100, null=False)
    studentemail = models.EmailField(max_length=100)
    studentage = models.IntegerField()
    trackname = models.CharField(max_length=100)

class Myuser(models.Model):
    id = models.AutoField(primary_key=True)
    myusername = models.CharField(max_length=100, null=True)
    userEmail = models.EmailField(max_length=100, null=True)
    userPass = models.CharField(max_length=15, null=True)

class Track(models.Model):
    trackname = models.CharField(max_length=20)