# Generated by Django 4.0.6 on 2022-07-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_variation_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('discount_percentage', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('num_available', models.IntegerField(default=1)),
                ('num_used', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='stock_levels',
            field=models.IntegerField(default=0),
        ),
    ]
