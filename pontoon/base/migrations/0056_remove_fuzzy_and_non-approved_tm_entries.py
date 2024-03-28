# Generated by Django 3.2.24 on 2024-03-28 10:39

from django.db import migrations


def remove_unused_tm_entries(apps, schema_editor):
    """Remove TM entries that belong to fuzzy Translations and Translations that are not approved."""
    TranslationMemoryEntry = apps.get_model("base", "TranslationMemoryEntry")

    TranslationMemoryEntry.objects.filter(translation__fuzzy=True).delete()
    TranslationMemoryEntry.objects.filter(translation__approved=False).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0055_populate_resource_order"),
    ]

    operations = [
        migrations.RunPython(
            code=remove_unused_tm_entries,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
