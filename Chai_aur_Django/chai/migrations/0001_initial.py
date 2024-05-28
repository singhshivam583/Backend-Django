# Generated by Django 5.0.6 on 2024-05-28 06:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChaiVarity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="chaiImage/")),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("BT", "Black Tea"),
                            ("GT", "Green Tea"),
                            ("ET", "Elaichi Tea"),
                            ("PT", "Plain Tea"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
