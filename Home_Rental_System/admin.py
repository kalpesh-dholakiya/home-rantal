from django.contrib import admin

# Register your models here.
from Home_Rental_System.models import Registration
admin.site.register(Registration)

from Home_Rental_System.models import Country
admin.site.register(Country)

from Home_Rental_System.models import State
admin.site.register(State)

from Home_Rental_System.models import City
admin.site.register(City)

from Home_Rental_System.models import Property
admin.site.register(Property)

from Home_Rental_System.models import Image
admin.site.register(Image)

from Home_Rental_System.models import Property_Type
admin.site.register(Property_Type)

from Home_Rental_System.models import Amenities
admin.site.register(Amenities)

from Home_Rental_System.models import AmenitiesAssing
admin.site.register(AmenitiesAssing)

from Home_Rental_System.models import Booking
admin.site.register(Booking)

from Home_Rental_System.models import Rating
admin.site.register(Rating)

from Home_Rental_System.models import Review
admin.site.register(Review)

from Home_Rental_System.models import Payment
admin.site.register(Payment)

