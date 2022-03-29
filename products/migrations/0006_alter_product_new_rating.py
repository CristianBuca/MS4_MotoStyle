# Generated by Django 3.2 on 2022-03-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_new_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
    ]