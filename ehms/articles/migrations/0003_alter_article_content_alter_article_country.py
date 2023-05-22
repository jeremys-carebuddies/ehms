# Generated by Django 4.1.9 on 2023-05-19 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("addresses", "0002_alter_region_options_alter_town_options"),
        ("articles", "0002_article_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(verbose_name="Content"),
        ),
        migrations.AlterField(
            model_name="article",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="article_country",
                to="addresses.country",
                verbose_name="Country",
            ),
        ),
    ]