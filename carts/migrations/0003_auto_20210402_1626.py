# Generated by Django 3.1.7 on 2021-04-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
