# Generated by Django 4.1.3 on 2022-11-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rival',
            field=models.CharField(default='', max_length=40),
        ),
    ]
