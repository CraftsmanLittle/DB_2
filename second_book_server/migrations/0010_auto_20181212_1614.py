# Generated by Django 2.1.4 on 2018-12-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0009_auto_20181212_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateField(),
        ),
    ]