# Generated by Django 3.0.5 on 2020-04-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
