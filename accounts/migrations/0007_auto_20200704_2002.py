# Generated by Django 3.0.8 on 2020-07-04 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200702_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'ordering': ['-updated', '-timestamp']},
        ),
    ]