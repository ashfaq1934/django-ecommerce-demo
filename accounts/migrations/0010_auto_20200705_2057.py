# Generated by Django 3.0.8 on 2020-07-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200705_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdefaultaddress',
            name='address',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='userdefaultaddress',
            name='county',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='userdefaultaddress',
            name='phone_number',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='userdefaultaddress',
            name='postal_code',
            field=models.CharField(max_length=120),
        ),
    ]