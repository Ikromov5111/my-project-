from ast import Global
from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse 
#from geography.models import ZipCode
# Create your models here.

class Hotel(models.Model):
    YULDUZLAR_SONI = {
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    }
    name = models.CharField( max_length=50)
    address = models.CharField(max_length = 50)
    room_qty = models.PositiveIntegerField()
    ochilgan_sana = models.DateField(null=True)  
    yulduzlar_soni = models.CharField(max_length =2,choices= YULDUZLAR_SONI)
    telefon_raqam = models.CharField(max_length=16)
    qushimcha_malumot = models.TextField()
    added_time = models.DateTimeField( auto_now=True)
    # zip_code = models.ForeignKey(
    #     ZipCode,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    # )
    def __str__(self):
        return self.name
    
class Worker(models.Model):
    STATUS_WORKER = [
        ("admin","admin"),
        ("menager","menager"),
        ("cooking", "cooling"),
        ("one", "one"),
        ("tue", "tue")
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone = models.CharField(max_length=18)
    pasport_serias = models.CharField(max_length=9)
    email = models.EmailField()
    adress = models.CharField(max_length=60)
    added_time = models.DateField(auto_now_add=True) 
    status_worker = models.CharField(max_length= 9,choices =STATUS_WORKER )
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
# class Article(models.Model):
#     title = models.CharField(max_length = 150)
#     summary = models.CharField(max_length= 200,blank = True)
#     body = models.TextField()
#     photo = models.ImageField(upload_to ='images/' , height_field=100, width_field=100)
#     date = models.DateTimeField(auto_now_add = True)
#     author = models.ForeignKey(
#         get_user_model(),
#         on_delete = models.CASCADE
#     )
 
#     def __str__(self):
#         return self.title
    
     
#     def get_absolute_url(self):
#         return reverse("article_detail", agrs=[str(self.id)])
    
        
class Room(models.Model):
    global Bolinmalar
    Bolinmalar = [
        ("1-kishilik","1-kishilik" ),
        ("2-kishilik", "2-kishilik"),
        ("3-kishilik", "3-kishilik"),
        ("4-kishilik", "4-kishilik"),
        ("5-kishilik", "5-kishilik"),
        
    ]
      
    IJARA = [
        ("YES","YES" ),
         ("NO","NO" ),
        
        
    ]
    number = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to = 'images/', blank = True)
    types = models.CharField(max_length=11,choices= Bolinmalar)
    bandligi = models.CharField(max_length=15, choices = IJARA)
    
    
    
class Ijara(models.Model):
    ijarachi = models.CharField(max_length=100)
    passport_serias = models.CharField(max_length=9)
    ijaraga_olinadigan_kun = models.DateTimeField()
    ijaradan_chiqadigan_kun = models.DateTimeField()
    person_qty = models.CharField( max_length=11, choices=Bolinmalar)
    room_num = models.ForeignKey(Room, on_delete=models.CASCADE,null = True)
    ijarachi = models.CharField(max_length=100)
    passport_serias = models.CharField(max_length=9)
    