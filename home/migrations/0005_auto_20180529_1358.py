# Generated by Django 2.0.5 on 2018-05-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180528_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='price',
            field=models.IntegerField(),
        ),
    ]
