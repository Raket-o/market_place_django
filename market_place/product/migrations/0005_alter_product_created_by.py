# Generated by Django 5.1.2 on 2024-10-16 21:26

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_product_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_by",
            field=models.CharField(default=django.contrib.auth.models.User),
        ),
    ]
