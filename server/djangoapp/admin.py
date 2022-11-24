from django.contrib import admin 
# <HINT> Import any new Models here

# from .models import related models
from .models import CarMake, CarModel

 
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name'] 


class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)