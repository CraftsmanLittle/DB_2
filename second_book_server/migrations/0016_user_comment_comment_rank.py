# Generated by Django 2.1.4 on 2018-12-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0015_auto_20181213_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_comment',
            name='comment_rank',
            field=models.IntegerField(default=5),
        ),
    ]