# Generated by Django 3.0.8 on 2020-07-07 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200705_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
    ]
