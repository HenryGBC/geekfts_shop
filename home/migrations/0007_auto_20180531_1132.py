# Generated by Django 2.0.5 on 2018-05-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180530_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Pagado'), ('received', 'Recibido'), ('in-process', 'En Proceso'), ('cancel', 'Cancelado'), ('sent', 'Enviado')], max_length=20),
        ),
    ]
