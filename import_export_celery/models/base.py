
from django.db import models

from django.utils.translation import gettext_lazy as _
from author.decorators import with_author


class BaseJob(models.Model):
    processing_initiated = models.DateTimeField(
        verbose_name=_("Have we started processing the file? If so when?"),
        null=True,
        blank=True,
        default=None,
    )

    processing_finished_at = models.DateTimeField(
        verbose_name=_("Have we finished processing the file? If so when?"),
        null=True,
        blank=True,
        default=None,
    )

    job_status = models.CharField(
        verbose_name=_("Status of the job"),
        max_length=160,
        blank=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")
