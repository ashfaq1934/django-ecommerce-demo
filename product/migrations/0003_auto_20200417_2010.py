# Generated by Django 3.0.5 on 2020-04-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200416_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=models.CharField(default='product_{<built-in function id>}', max_length=120), unique=True),
        ),
    ]
