# Generated by Django 2.1.4 on 2018-12-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0033_activity_pecent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
