# Generated by Django 2.0.5 on 2018-05-31 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_shirtcolor_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShirtColor',
            new_name='ShirtOrder',
        ),
    ]
