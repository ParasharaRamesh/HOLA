# Generated by Django 2.1.1 on 2018-10-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holaserver', '0008_auto_20181005_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertable',
            name='customerId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driverdetailstable',
            name='driverId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
