# Generated by Django 4.1.9 on 2023-05-14 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("hospitals", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserRequest",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "status",
                    model_utils.fields.StatusField(
                        choices=[("active", "active"), ("inactive", "inactive")],
                        default="active",
                        max_length=100,
                        no_check_for_status=True,
                        verbose_name="status",
                    ),
                ),
                (
                    "status_changed",
                    model_utils.fields.MonitorField(
                        default=django.utils.timezone.now, monitor="status", verbose_name="status changed"
                    ),
                ),
                (
                    "id",
                    model_utils.fields.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("request_id", models.CharField(blank=True, max_length=255, unique=True, verbose_name="Request Id")),
                ("user_level", models.CharField(max_length=255, verbose_name="User Level")),
                ("description", models.TextField(max_length=10000000, verbose_name="Describe the changes")),
                (
                    "document",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="patient_document_upload",
                        verbose_name="Upload relevant document",
                    ),
                ),
                (
                    "response_status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("In process", "In process"),
                            ("Rejected", "Rejected"),
                            ("Completed", "Completed"),
                        ],
                        default="Pending",
                        max_length=10,
                        verbose_name="Response status",
                    ),
                ),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="user_request_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="user_request_hospital",
                        to="hospitals.hospital",
                        verbose_name="Hospital",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Request",
                "verbose_name_plural": "User Reuests",
            },
        ),
        migrations.CreateModel(
            name="UserReport",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "status",
                    model_utils.fields.StatusField(
                        choices=[("active", "active"), ("inactive", "inactive")],
                        default="active",
                        max_length=100,
                        no_check_for_status=True,
                        verbose_name="status",
                    ),
                ),
                (
                    "status_changed",
                    model_utils.fields.MonitorField(
                        default=django.utils.timezone.now, monitor="status", verbose_name="status changed"
                    ),
                ),
                (
                    "id",
                    model_utils.fields.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("report_id", models.CharField(blank=True, max_length=255, unique=True, verbose_name="Request Id")),
                ("user_level", models.CharField(max_length=255, verbose_name="User Level")),
                ("section", models.CharField(max_length=255, verbose_name="Section")),
                ("description", models.TextField(max_length=10000000, verbose_name="Describe the changes")),
                (
                    "response_status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("In process", "In process"),
                            ("Rejected", "Rejected"),
                            ("Completed", "Completed"),
                        ],
                        default="Pending",
                        max_length=10,
                        verbose_name="Response status",
                    ),
                ),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="user_report_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="user_report_hospital",
                        to="hospitals.hospital",
                        verbose_name="Hospital",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Report",
                "verbose_name_plural": "User Reports",
            },
        ),
    ]
