# Generated by Django 3.1.5 on 2021-01-15 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventDetails',
            new_name='EventDetail',
        ),
    ]
