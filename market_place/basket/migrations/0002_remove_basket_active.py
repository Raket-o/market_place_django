# Generated by Django 5.1.2 on 2024-10-24 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("basket", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="basket",
            name="active",
        ),
    ]
