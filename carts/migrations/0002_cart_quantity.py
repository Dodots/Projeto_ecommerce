# Generated by Django 3.1.7 on 2021-04-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
