# Generated by Django 3.2.7 on 2021-11-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vmental", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customizeduser",
            name="gender",
            field=models.CharField(
                blank=True, choices=[("M", "Male"), ("F", "Female")], max_length=1
            ),
        ),
    ]
