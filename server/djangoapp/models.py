import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.conf import settings
import uuid


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
 


class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    # Add
    country = models.CharField(max_length=50)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description  + "," + \
               "Country: " + self.country    


# # <HINT> Create a Car Model model `class CarModel(models.Model):`:
# # - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# # - Name
# # - Dealer id, used to refer a dealer created in cloudant database
# # - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# # - Year (DateField)
# # - Any other fields you would like to include in car model
# # - __str__ method to print a car make object
# # Lesson model


# class CarModel(models.Model):
class CarModel(models.Model):
    name = models.CharField(max_length=30)
    dealer_id = models.IntegerField(default=0)
    
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    CHEVY = 'chevy'
    UNKNOWN = 'UNKNOWN'

    CARS_MODELS = [
        (SEDAN, 'Sedan'),
        (SUV, 'Suv'),
        (WAGON, 'Wagon'),
        (CHEVY, 'Chevy'),  
        (UNKNOWN, 'UNKNOWN')
    ]
    type_model = models.CharField(max_length=20, choices=CARS_MODELS, default=UNKNOWN)
    year = models.DateField(null=True)

    # Add
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    price = models.FloatField(default=10000)
     
               
# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data


 
 
