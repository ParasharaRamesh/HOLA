# Generated by Django 2.1.1 on 2018-10-02 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holaserver', '0004_remove_carstatustable_cartype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetailstable',
            name='carId',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='holaserver.CarStatusTable', verbose_name='carId'),
        ),
    ]