# Generated by Django 3.0.8 on 2020-07-05 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200704_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='billing',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='shipping',
        ),
    ]
