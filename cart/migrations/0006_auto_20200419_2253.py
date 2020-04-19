# Generated by Django 3.0.5 on 2020-04-19 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200417_2010'),
        ('cart', '0005_auto_20200419_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='product.Product'),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]