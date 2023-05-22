# Generated by Django 4.1.9 on 2023-05-14 14:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ehms.inventory.models
import model_utils.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("hospitals", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("medical_sessions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Supplier",
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
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                ("company", models.CharField(max_length=200, verbose_name="Company")),
                ("email", models.EmailField(blank=True, max_length=100, verbose_name="Email")),
                ("phone", models.CharField(max_length=12, verbose_name="Phone")),
                ("alternate_phone", models.CharField(blank=True, max_length=12, verbose_name="Alternate phone")),
                ("address_line_1", models.CharField(max_length=200, verbose_name="Address Line 1")),
                (
                    "address_line_2",
                    models.CharField(
                        blank=True, help_text="Landmark near by, if any", max_length=200, verbose_name="Address Line 2"
                    ),
                ),
                ("city", models.CharField(max_length=200, verbose_name="City")),
                ("country", models.CharField(max_length=200, verbose_name="Country")),
                ("postcode", models.CharField(max_length=200, verbose_name="Postcode")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=ehms.inventory.models.supplier_image_upload,
                        verbose_name="Supplier Image",
                    ),
                ),
                ("remarks", models.TextField(blank=True, verbose_name="Remarks")),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="supplier_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Supplier",
                "verbose_name_plural": "Suppliers",
            },
        ),
        migrations.CreateModel(
            name="ReceivedDetail",
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
                ("bill_number", models.CharField(blank=True, max_length=12, unique=True, verbose_name="Bill Number")),
                ("total_items", models.PositiveSmallIntegerField(verbose_name="Total items")),
                (
                    "gross_amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Total amount of the received items.",
                        max_digits=9,
                        null=True,
                        verbose_name="Gross Amount",
                    ),
                ),
                (
                    "remarks",
                    models.TextField(
                        blank=True,
                        help_text="Write something important against received items.",
                        max_length=10000,
                        verbose_name="Remarks",
                    ),
                ),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="received_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="received_hospital",
                        to="hospitals.hospital",
                        verbose_name="Hospital",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="supplier_of_item",
                        to="inventory.supplier",
                        verbose_name="Supplier",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ItemCategory",
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
                ("name", models.CharField(max_length=200, unique=True, verbose_name="Name")),
                ("description", models.TextField(blank=True, verbose_name="Description")),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="item_category_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Item Category",
                "verbose_name_plural": "Item Categories",
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("item_name", models.CharField(max_length=200, unique=True, verbose_name="Item Name")),
                ("sku", models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name="SKU")),
                (
                    "market_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True, verbose_name="Market Price"
                    ),
                ),
                (
                    "selling_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True, verbose_name="Selling Price"
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Description")),
                (
                    "minimum_stock_value",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(100000000),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="Minimum Stock Value",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=ehms.inventory.models.item_image_upload,
                        verbose_name="Item Image",
                    ),
                ),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="item_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
                (
                    "item_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="item_category",
                        to="inventory.itemcategory",
                        verbose_name="Item Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Items",
            },
        ),
        migrations.CreateModel(
            name="IssuedDetail",
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
                ("bill_number", models.CharField(blank=True, max_length=12, unique=True, verbose_name="Bill Number")),
                (
                    "gross_amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Total amount of the issued items.",
                        max_digits=9,
                        null=True,
                        verbose_name="Gross Amount",
                    ),
                ),
                ("total_items", models.PositiveSmallIntegerField(verbose_name="Total items")),
                (
                    "remarks",
                    models.TextField(
                        blank=True,
                        help_text="Write something important against issued items.",
                        max_length=10000,
                        verbose_name="Remarks",
                    ),
                ),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="issued_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="issued_department",
                        to="medical_sessions.department",
                        verbose_name="Department",
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="issued_hospital",
                        to="hospitals.hospital",
                        verbose_name="Hospital",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Inventory",
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
                ("type", models.CharField(default="Stock In", max_length=200, verbose_name="Type")),
                (
                    "received_quantity",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Quantity is like a unit.",
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(100000000),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="Received Quantity",
                    ),
                ),
                (
                    "issued_quantity",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Quantity is like a unit.",
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(100000000),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="Issued Quantity",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="The price here will be per unit.",
                        max_digits=9,
                        null=True,
                        verbose_name="Item Price",
                    ),
                ),
                (
                    "vat",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Mention the price not the percentage.",
                        max_digits=9,
                        null=True,
                        verbose_name="Vat",
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Mention the price not the percentage.",
                        max_digits=9,
                        null=True,
                        verbose_name="Discount",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Price of all the units i.e. entire quantity.",
                        max_digits=9,
                        null=True,
                        verbose_name="Total Price",
                    ),
                ),
                (
                    "remarks",
                    models.TextField(
                        blank=True,
                        help_text="Write something important against item.",
                        max_length=10000,
                        verbose_name="Remarks",
                    ),
                ),
                (
                    "creator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="inventory_creator_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Logged in user",
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="inventory_hospital",
                        to="hospitals.hospital",
                        verbose_name="Hospital",
                    ),
                ),
                (
                    "issued_detail",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="inventory_issue_detail",
                        to="inventory.issueddetail",
                        verbose_name="Issued Detail",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="inventory_item",
                        to="inventory.item",
                        verbose_name="Item",
                    ),
                ),
                (
                    "item_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="inventory_item_category",
                        to="inventory.itemcategory",
                        verbose_name="Item Category",
                    ),
                ),
                (
                    "received_detail",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="inventory_receive_detail",
                        to="inventory.receiveddetail",
                        verbose_name="Received Detail",
                    ),
                ),
            ],
            options={
                "verbose_name": "Inventory",
                "verbose_name_plural": "Inventory",
            },
        ),
    ]