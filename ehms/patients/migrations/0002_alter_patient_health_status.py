# Generated by Django 4.1.9 on 2023-05-15 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="health_status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="patient_health_status",
                to="patients.healthstatus",
                verbose_name="Health Status",
            ),
        ),
    ]
