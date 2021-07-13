# Generated by Django 3.1.1 on 2020-09-20 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Rental_System', '0002_auto_20200920_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home_Rental_System.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home_Rental_System.state')),
            ],
        ),
    ]