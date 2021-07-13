from django.db import models

# Create your models here.

class Registration(models.Model):
    email_id=models.EmailField(max_length=50,primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    gender=models.IntegerField()
    phone_no=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=15)
    user_type=models.IntegerField()

'''class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

class State(models.Model):
    state_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)    
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)

class Property(models.Model):
    property_id=models.IntegerField()
    email_id=models.ForeignKey(Registration,on_delete=models.CASCADE)
    property_name=models.CharField(max_length=20)
    property_type=models.IntegerField()
    rent=models.IntegerField()
    address=models.CharField(max_length=100)
    city_id=models.IntegerField()
    map=models.CharField(max_length=50)
    status=models.IntegerField()
    bedroom=models.IntegerField()
    description=models.CharField(max_length=256)
    washroom=models.IntegerField()'''
