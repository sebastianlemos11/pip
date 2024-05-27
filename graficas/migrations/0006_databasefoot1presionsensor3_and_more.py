# Generated by Django 5.0.6 on 2024-05-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graficas', '0005_databasefoot1presion'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBaseFoot1PresionSensor3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataBaseFoot1PresionSensor4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataBaseFoot1PresionSensor5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataBaseFoot1Sensor1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataBaseFoot1Sensor2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataBaseFoot1Sensor3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataBaseFoot1Sensor4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataBaseFoot1Sensor5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='DataBaseFoot1Presion',
            new_name='DataBaseFoot1PresionSensor1',
        ),
        migrations.RenameModel(
            old_name='DataBaseFoot1',
            new_name='DataBaseFoot1PresionSensor2',
        ),
    ]
