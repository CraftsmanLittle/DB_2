# Generated by Django 2.1.4 on 2018-12-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0038_auto_20181219_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='price',
            field=models.FloatField(default='80'),
        ),
    ]
