# Generated by Django 3.2.15 on 2023-11-22 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0050_strings_xml_apostrophes"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocaleCodeHistory",
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
                ("old_code", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "locale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.locale"
                    ),
                ),
            ],
        ),
    ]