# Generated by Django 2.0.5 on 2018-05-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180531_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirtorder',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
