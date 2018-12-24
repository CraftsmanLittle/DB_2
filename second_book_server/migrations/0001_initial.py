# Generated by Django 2.1.4 on 2018-12-08 09:08

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='Register time')),
                ('user_nickname', models.CharField(default='', max_length=30)),
                ('university_name', models.CharField(default='', max_length=30)),
                ('user_profile', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
