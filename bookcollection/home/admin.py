from django.contrib import admin
from .models.model import Product
from .models.category import Categorie
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Categorie, AdminCategory)
admin.site.register(Customer,AdminCustomer)
