# Generated by Django 3.2.7 on 2021-11-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointments",
            name="status",
            field=models.CharField(
                choices=[("confirmed", "confirmed"), ("available", "available")],
                default="draft",
                max_length=10,
            ),
        ),
    ]
