# Generated by Django 2.1.4 on 2018-12-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0004_auto_20181211_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_comment',
            name='date',
            field=models.DateField(),
        ),
    ]
