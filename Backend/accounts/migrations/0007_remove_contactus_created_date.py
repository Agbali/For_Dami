# Generated by Django 4.1 on 2022-08-10 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='created_date',
        ),
    ]
