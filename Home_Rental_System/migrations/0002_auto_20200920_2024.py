# Generated by Django 3.1.1 on 2020-09-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Rental_System', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='user_type',
            field=models.IntegerField(),
        ),
    ]
