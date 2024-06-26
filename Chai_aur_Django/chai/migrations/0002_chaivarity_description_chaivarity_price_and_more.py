# Generated by Django 5.0.6 on 2024-05-28 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chai", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chaivarity",
            name="description",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="chaivarity",
            name="price",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="chaivarity",
            name="type",
            field=models.CharField(
                choices=[
                    ("BT", "Black Tea"),
                    ("MT", "Masala Tea"),
                    ("ET", "Elaichi Tea"),
                    ("PT", "Plain Tea"),
                    ("GT", "Ginger Tea"),
                ],
                max_length=2,
            ),
        ),
    ]
