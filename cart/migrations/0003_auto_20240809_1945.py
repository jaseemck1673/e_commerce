# Generated by Django 2.2 on 2024-08-09 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20240805_2356'),
        ('cart', '0002_cartitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cartItems',
            new_name='items',
        ),
        migrations.RenameField(
            model_name='cartlist',
            old_name='car_id',
            new_name='cart_id',
        ),
        migrations.AlterField(
            model_name='items',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist'),
        ),
    ]