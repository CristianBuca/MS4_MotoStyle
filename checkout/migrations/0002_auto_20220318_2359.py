# Generated by Django 3.2 on 2022-03-18 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='county',
            new_name='address_line2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address2',
            new_name='area',
        ),
    ]
