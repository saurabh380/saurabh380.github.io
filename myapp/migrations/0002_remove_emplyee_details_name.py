# Generated by Django 3.0.6 on 2020-11-01 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emplyee_details',
            name='name',
        ),
    ]
