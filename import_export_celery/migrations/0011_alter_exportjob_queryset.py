# Generated by Django 5.0.7 on 2024-07-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("import_export_celery", "0010_auto_20231013_0904"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exportjob",
            name="queryset",
            field=models.JSONField(
                verbose_name="JSON list of pks to export or dict of queryset filters"
            ),
        ),
    ]