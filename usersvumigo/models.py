from django.db import models


class VumiGoUser(models.Model):
    msisdn = models.CharField(max_length=30,
                              blank=False,
                              verbose_name="MSISDN (Mobile Number)")
    sex = models.CharField(max_length=6)
    age = models.CharField(max_length=30)
    community = models.CharField(max_length=30)

    def __unicode__(self):
        return self.msisdn

    class Meta:
        verbose_name = "User"