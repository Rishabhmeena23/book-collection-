from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=90)




    @staticmethod
    def get_all_category():
        return Categorie.objects.all()
        
    def __str__(self):
         return self.name

