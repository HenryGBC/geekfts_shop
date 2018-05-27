# Generated by Django 2.0.5 on 2018-05-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='shirt',
            name='size',
        ),
        migrations.AddField(
            model_name='shirt',
            name='size',
            field=models.ManyToManyField(to='home.Size'),
        ),
    ]
