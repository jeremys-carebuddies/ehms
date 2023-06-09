# Generated by Django 4.1.9 on 2023-05-14 14:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("hospitals", "0001_initial"),
        ("patients", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Mortuary",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
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
                ("uid", models.CharField(blank=True, max_length=255, unique=True, verbose_name="UID")),
                ("name", models.CharField(max_length=200, verbose_name="Name of Mortuary")),
                (
                    "capacity",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(1000),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="Capacity",
                    ),
                ),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="mortuary_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="mortuary_hospital",
                        to="hospitals.hospital",
                        verbose_name="Hospital",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mortuary",
                "verbose_name_plural": "Mortuaries",
            },
        ),
        migrations.CreateModel(
            name="MortuaryPatient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
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
                    "tag",
                    models.CharField(
                        max_length=18, unique=True, verbose_name="Random tag generated against deceased patient"
                    ),
                ),
                (
                    "date_received",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Mortuary entry date of deceased patient"
                    ),
                ),
                (
                    "date_released",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Mortuary released date of deceased patient"
                    ),
                ),
                ("reason_behind_release", models.TextField(verbose_name="Reason behind release of deceased patient")),
                ("in_mortuary", models.BooleanField(default=True, verbose_name="Is deceased patient in mortuary?")),
                (
                    "next_of_kin",
                    models.CharField(blank=True, max_length=200, verbose_name="Deceased patient next of kin name"),
                ),
                (
                    "next_of_kin_relationship",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Great Grand Father", "Great Grand Father"),
                            ("Grand Father", "Grand Father"),
                            ("Father", "Father"),
                            ("Step-Father", "Step-Father"),
                            ("Great Grand Mother", "Great Grand Mother"),
                            ("Grand Mother", "Grand Mother"),
                            ("Mother", "Mother"),
                            ("Step-Mother", "Step-Mother"),
                            ("Daughter", "Daughter"),
                            ("Son", "Son"),
                            ("Wife", "Wife"),
                            ("Husband", "Husband"),
                            ("Child", "Child"),
                            ("Brother", "Brother"),
                            ("Sister", "Sister"),
                            ("Grand Son", "Grand Son"),
                            ("Grand Daughter", "Grand Daughter"),
                            ("Step-Child", "Step-Child"),
                            ("Adopted Child", "Adopted Child"),
                            ("Mother-in-law", "Mother-in-law"),
                            ("Father-in-law", "Father-in-law"),
                            ("Daughter-in-law", "Daughter-in-law"),
                            ("Brother-in-law", "Brother-in-law"),
                            ("Sister-in-law", "Sister-in-law"),
                            ("Uncle", "Uncle"),
                            ("Aunt", "Aunt"),
                            ("Nephew", "Nephew"),
                            ("Niece", "Niece"),
                            ("Other", "Other"),
                        ],
                        max_length=100,
                        verbose_name="Next of kin relationship to deceased patient",
                    ),
                ),
                (
                    "non_relative_person",
                    models.CharField(blank=True, max_length=200, verbose_name="Non relative person name"),
                ),
                (
                    "person_address",
                    models.TextField(
                        help_text="Provide address of who ever released the deceased patient",
                        verbose_name="Person address",
                    ),
                ),
                (
                    "person_phone",
                    models.CharField(
                        help_text="Provide phone of who ever released the deceased patient",
                        max_length=12,
                        verbose_name="Person phone",
                    ),
                ),
                (
                    "witness",
                    models.CharField(
                        blank=True,
                        help_text="Witness during the release of the deceased patient",
                        max_length=200,
                        verbose_name="Witness name",
                    ),
                ),
                (
                    "witness_address",
                    models.TextField(blank=True, help_text="Witness address", verbose_name="Witness address"),
                ),
                (
                    "witness_phone",
                    models.CharField(
                        blank=True, help_text="Witness phone", max_length=12, verbose_name="Witness phone"
                    ),
                ),
                ("person_uid", models.CharField(blank=True, max_length=12, verbose_name="Person UID if available")),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="mortuary_patient_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="mortuary_patient_hospital",
                        to="hospitals.hospital",
                        verbose_name="Hospital",
                    ),
                ),
                (
                    "mortuary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="mortuary_patient_mortuary",
                        to="mortuaries.mortuary",
                        verbose_name="Mortuary",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="mortuary_patient_belongs_to_patient",
                        to="patients.patient",
                        verbose_name="Patient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mortuary Patient",
                "verbose_name_plural": "Mortuary Patients",
            },
        ),
    ]
