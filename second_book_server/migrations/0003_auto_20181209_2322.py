# Generated by Django 2.1.4 on 2018-12-09 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0002_auto_20181208_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('begin_time', models.DateField(auto_now_add=True)),
                ('end_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Activity_price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activity_id', models.ManyToManyField(to='second_book_server.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('an_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('an_title', models.CharField(max_length=50)),
                ('an_content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bool_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('book_name', models.TextField(unique=True)),
                ('publish_time', models.DateField(null=True)),
                ('book_version', models.CharField(max_length=15)),
                ('author', models.TextField(null=True)),
                ('publish_house', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Chat_record',
            fields=[
                ('record_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('sender_id', models.CharField(max_length=30)),
                ('receiver_id', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('date_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('Coupon_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('coupon_name', models.CharField(max_length=50)),
                ('credits', models.DecimalField(decimal_places=5, max_digits=5)),
                ('begin_time', models.DateField(auto_now_add=True)),
                ('end_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('Label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('goods_time', models.DateField()),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('introduction', models.TextField()),
                ('subject', models.TextField()),
                ('amount', models.IntegerField()),
                ('book_id', models.ManyToManyField(to='second_book_server.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Logininformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_time', models.DateField(auto_now_add=True)),
                ('log_ip', models.GenericIPAddressField()),
                ('log_outtime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ordersheet',
            fields=[
                ('order_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('buyer_id', models.CharField(max_length=30)),
                ('Seller_id', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=10)),
                ('is_paid', models.BooleanField()),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_book_server.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_book_server.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='User_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.TextField(null=True)),
                ('address_2', models.TextField(null=True)),
                ('address_3', models.TextField(null=True)),
                ('address_4', models.TextField(null=True)),
                ('address_5', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='系统默认好评')),
                ('date', models.DateField(auto_now_add=True)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_book_server.Goods')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user_address',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shopping_cart',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='logininformation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='goods',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favorites',
            name='goods_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_book_server.Goods'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity_price',
            name='goods_id',
            field=models.ManyToManyField(to='second_book_server.Goods'),
        ),
    ]
