# Generated by Django 3.2.7 on 2021-11-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20211031_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'published'), ('draft', 'draft')], default='draft', max_length=10),
        ),
    ]
