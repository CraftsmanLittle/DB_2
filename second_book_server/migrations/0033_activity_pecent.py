# Generated by Django 2.1.4 on 2018-12-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0032_auto_20181218_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='pecent',
            field=models.FloatField(default='1'),
        ),
    ]
