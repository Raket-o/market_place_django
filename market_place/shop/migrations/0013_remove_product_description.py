# Generated by Django 5.1.2 on 2024-10-31 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0012_alter_product_photo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="description",
        ),
    ]