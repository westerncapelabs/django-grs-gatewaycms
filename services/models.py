from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=125, blank=False)
    content_1 = models.CharField(max_length=125, blank=True)
    content_2 = models.CharField(max_length=125, blank=True)
    content_3 = models.CharField(max_length=125, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Service"
