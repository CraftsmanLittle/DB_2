# Generated by Django 2.1.4 on 2018-12-12 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0007_goods_goods_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='book_id',
        ),
        migrations.AddField(
            model_name='goods',
            name='book_id',
            field=models.ForeignKey(default=1994, on_delete=django.db.models.deletion.CASCADE, to='second_book_server.Book'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='goods',
            name='user_id',
        ),
        migrations.AddField(
            model_name='goods',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
