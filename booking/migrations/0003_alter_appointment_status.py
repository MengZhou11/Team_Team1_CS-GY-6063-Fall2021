# Generated by Django 3.2.9 on 2021-12-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0002_alter_appointment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="status",
            field=models.CharField(
                choices=[("active", "active"), ("cancelled", "cancelled")],
                default="active",
                max_length=10,
            ),
        ),
    ]
