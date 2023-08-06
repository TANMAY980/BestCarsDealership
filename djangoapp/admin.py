from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
# CarModelAdmin class
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
# CarMakeAdmin class with CarModelInline
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [CarModelInline]

# Register models here
