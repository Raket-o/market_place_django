# Generated by Django 5.1.2 on 2024-10-24 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("basket", "0003_alter_basket_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="basket",
            name="quantity",
        ),
    ]