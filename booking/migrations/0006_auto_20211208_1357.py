# Generated by Django 3.2.9 on 2021-12-08 18:57

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0005_auto_20211208_1354"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="end_time",
            field=models.TimeField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=models.TimeField(
                            validators=[
                                django.core.validators.MinValueValidator(
                                    limit_value=datetime.time(13, 57, 46, 198899)
                                )
                            ]
                        )
                    )
                ]
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="start_time",
            field=models.TimeField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.time(13, 57, 46, 198899)
                    )
                ]
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="status",
            field=models.CharField(
                choices=[
                    ("cancelled", "cancelled"),
                    ("expired", "expired"),
                    ("active", "active"),
                ],
                default="active",
                max_length=10,
            ),
        ),
    ]
