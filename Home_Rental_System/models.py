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

class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

class State(models.Model):
    state_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)    
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)

class City(models.Model):
    city_id=models.IntegerField(primary_key=True)    
    name=models.CharField(max_length=50)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE)
    image=models.CharField(max_length=100)

class Property_Type(models.Model):
    property_type_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

class Property(models.Model):
    property_id=models.IntegerField(primary_key=True)
    email_id=models.ForeignKey(Registration,on_delete=models.CASCADE)
    property_name=models.CharField(max_length=20)
    property_type=models.ForeignKey(Property_Type,on_delete=models.CASCADE)
    rent=models.IntegerField()
    address=models.CharField(max_length=100)
    city_id=models.ForeignKey(City,on_delete=models.CASCADE)
    map1=models.CharField(max_length=50)
    status=models.IntegerField()
    bedroom=models.IntegerField()
    description=models.TextField(max_length=300)
    washroom=models.IntegerField()

class Image(models.Model):
    image_id=models.IntegerField(primary_key=True)
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE)
    image=models.CharField(max_length=100)    

class Amenities(models.Model):
    amenities_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

class AmenitiesAssing(models.Model):
    amenities_assign_id=models.IntegerField(primary_key=True)  
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE)
    amenities_id=models.ForeignKey(Amenities,on_delete=models.CASCADE)

class Booking(models.Model):
    booking_id=models.IntegerField(primary_key=True)
    email_id=models.ForeignKey(Registration,on_delete=models.CASCADE)
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE)
    check_in_date=models.DateField()
    check_out_date=models.DateField()
    status=models.IntegerField()

class Rating(models.Model):
    rating_id=models.IntegerField(primary_key=True)
    email_id=models.ForeignKey(Registration,on_delete=models.CASCADE)
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE) 
    rating=models.IntegerField()   

class Review(models.Model):
    review_id=models.IntegerField(primary_key=True)
    email_id=models.ForeignKey(Registration,on_delete=models.CASCADE)
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE) 
    review=models.CharField(max_length=200)

class Payment(models.Model):
    payment_id=models.IntegerField(primary_key=True)
    booking_id=models.ForeignKey(Booking,on_delete=models.CASCADE)
    amount=models.IntegerField()
    payment_date=models.DateField()
    payment_type=models.CharField(max_length=10)
    status=models.IntegerField()    