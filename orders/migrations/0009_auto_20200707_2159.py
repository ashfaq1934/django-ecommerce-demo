# Generated by Django 3.0.8 on 2020-07-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200707_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='address',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='city',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='county',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='phone_number',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='postal_code',
            field=models.CharField(max_length=120, null=True),
        ),
    ]