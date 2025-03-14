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

class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview:

    # def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year,id):
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year,sentiment, id):
        # Dealer address
        self.dealership = dealership
        # Dealer city
        self.name = name
        # Dealer Full Name
        self.purchase = purchase
        # Dealer id
        self.review = review
        # Location lat
        self.purchase_date = purchase_date
        # Location long
        self.car_make = car_make
        # Dealer short name
        self.car_model = car_model
        # Dealer state
        self.car_year = car_year
        # Dealer zip
        self.sentiment = sentiment
        # Dealer id
        self.id = id

    def __str__(self):
        return "Dealer review: " + self.name
 
 
