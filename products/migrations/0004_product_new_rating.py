# Generated by Django 3.2 on 2022-03-27 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
