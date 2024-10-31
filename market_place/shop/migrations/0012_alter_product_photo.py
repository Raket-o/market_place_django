# Generated by Django 5.1.2 on 2024-10-31 19:09

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0011_remove_product_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                null=True, upload_to=shop.models.prod_photo_directory_path
            ),
        ),
    ]
