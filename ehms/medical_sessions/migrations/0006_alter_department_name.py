# Generated by Django 4.1.9 on 2023-05-18 23:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medical_sessions", "0005_medicalsession_ipd_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(max_length=100, unique=True, verbose_name="Name"),
        ),
    ]
