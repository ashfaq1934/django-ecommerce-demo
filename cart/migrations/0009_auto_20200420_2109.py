# Generated by Django 3.0.5 on 2020-04-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_cartitem_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='notes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]