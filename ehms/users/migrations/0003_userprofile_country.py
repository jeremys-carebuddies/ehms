# Generated by Django 4.1.9 on 2023-05-19 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("addresses", "0002_alter_region_options_alter_town_options"),
        ("users", "0002_remove_userprofile_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="users_country",
                to="addresses.country",
                verbose_name="Country",
            ),
        ),
    ]