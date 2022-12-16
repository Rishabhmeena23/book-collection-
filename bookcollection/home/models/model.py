from django.db import models
from .category import Categorie


class Product(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=90)
    price = models.CharField(max_length=90)
    description = models.CharField(max_length=150, default='', null=True, blank=True)
    image = models.ImageField(upload_to='upload/products/', default='pixel.jpg')

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        return Product.objects.filter(category = category_id)

