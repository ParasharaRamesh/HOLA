# Generated by Django 2.1.2 on 2018-11-03 05:41

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetailsTable',
            fields=[
                ('carId', models.AutoField(primary_key=True, serialize=False)),
                ('carType', models.IntegerField(choices=[(1, 'UNKNOWN'), (2, 'CAR_TYPE_HATCHBACK'), (3, 'CAR_TYPE_SEDAN'), (4, 'CAR_TYPE_MINIVAN')], default=1)),
                ('carModel', models.CharField(max_length=64)),
                ('carLicense', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': 'CarDetailsTable',
            },
        ),
        migrations.CreateModel(
            name='CarStatusTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carAvailability', models.IntegerField(choices=[(1, 'UNKNOWN'), (2, 'CAR_OFF_DUTY'), (3, 'CAR_AVAILABLE'), (4, 'CAR_ON_TRIP'), (5, 'CAR_ON_TRIP_CLOSE_TO_COMPLETION')], default=1)),
                ('geoLocation', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('carId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest.CarDetailsTable', verbose_name='carId')),
            ],
            options={
                'verbose_name_plural': 'CarStatusTable',
            },
        ),
        migrations.CreateModel(
            name='DriverDetailsTable',
            fields=[
                ('driverId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=10)),
                ('carId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest.CarDetailsTable', verbose_name='carId')),
            ],
            options={
                'verbose_name_plural': 'DriverDetailsTable',
            },
        ),
        migrations.CreateModel(
            name='RatingTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('feedback', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'RatingTable',
            },
        ),
        migrations.CreateModel(
            name='TripTable',
            fields=[
                ('tripId', models.AutoField(primary_key=True, serialize=False)),
                ('sourceLocation', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('destinationLocation', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('startTimeInEpochs', models.PositiveIntegerField()),
                ('endTimeInEpochs', models.PositiveIntegerField(null=True)),
                ('tripPrice', models.FloatField()),
                ('tripStatus', models.IntegerField(choices=[(1, 'UNKNOWN'), (2, 'TRIP_STATUS_SCHEDULED'), (3, 'TRIP_STATUS_ONGOING'), (4, 'TRIP_STATUS_COMPLETED'), (5, 'TRIP_STATUS_CANCELLED')], default=1)),
                ('paymentMode', models.IntegerField(choices=[(1, 'UNKNOWN'), (2, 'CASH_PAYMENT'), (3, 'CARD_PAYMENT'), (4, 'PAYTM_PAYMENT')], default=1)),
                ('carId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest.CarDetailsTable', verbose_name='carId')),
                ('customerId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='customerId')),
                ('driverId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest.DriverDetailsTable', verbose_name='driverId')),
            ],
            options={
                'verbose_name_plural': 'TripTable',
            },
        ),
        migrations.AddField(
            model_name='ratingtable',
            name='tripId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest.TripTable', verbose_name='tripId'),
        ),
    ]
