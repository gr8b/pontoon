# Generated by Django 1.11.28 on 2020-03-08 19:52
import django.db.migrations.operations.special
import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("base", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Error",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "library",
                    models.CharField(
                        choices=[
                            ("p", "pontoon"),
                            ("cl", "compare-locales"),
                        ],
                        db_index=True,
                        max_length=20,
                    ),
                ),
                ("message", models.TextField()),
                (
                    "translation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="errors",
                        to="base.Translation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Warning",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "library",
                    models.CharField(
                        choices=[
                            ("p", "pontoon"),
                            ("cl", "compare-locales"),
                        ],
                        db_index=True,
                        max_length=20,
                    ),
                ),
                ("message", models.TextField()),
                (
                    "translation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="warnings",
                        to="base.Translation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterUniqueTogether(
            name="warning",
            unique_together={("translation", "library", "message")},
        ),
        migrations.AlterUniqueTogether(
            name="error",
            unique_together={("translation", "library", "message")},
        ),
    ]
