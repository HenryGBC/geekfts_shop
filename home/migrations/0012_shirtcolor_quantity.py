# Generated by Django 2.0.5 on 2018-05-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_shirtcolor_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirtcolor',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]