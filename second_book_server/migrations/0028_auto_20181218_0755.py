# Generated by Django 2.1.4 on 2018-12-17 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0027_ordersheet_coupon_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersheet',
            name='Seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ordersheet',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
    ]
