# Generated by Django 2.2.5 on 2019-09-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_export_celery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='importjob',
            name='job_status',
            field=models.CharField(blank=True, max_length=160, verbose_name='Status of the job'),
        ),
    ]
