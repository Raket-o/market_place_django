# Generated by Django 5.1.2 on 2024-10-26 12:53

import authorization.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authorization", "0002_profile_first_name_profile_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(
                default=4,
                max_length=20,
                validators=[authorization.models.validate_phone_number],
            ),
            preserve_default=False,
        ),
    ]