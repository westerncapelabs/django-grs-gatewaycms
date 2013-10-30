# Python
from random import randint

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class AirtimeApplication(models.Model):
    name = models.CharField(max_length=50)
    ratio  = models.IntegerField(null=True, blank=True)
    max_per_day  = models.IntegerField(null=True, blank=True)
    amount  = models.IntegerField(null=True, blank=True)
    active = models.BooleanField()
    product_key = models.CharField(max_length=10)
    notification_sms = models.CharField(max_length=160,
                                        null=True,
                                        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Airtime Application"

class SendAirtime(models.Model):
    app_id = models.ForeignKey(AirtimeApplication,
                               related_name="app_id")
    msisdn = models.CharField(max_length=30,
                              verbose_name="MSISDN (Mobile Number)")
    product_key = models.CharField(max_length=10)
    amount  = models.IntegerField()
    sent = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True,
                                      blank=False,
                                      editable=False)

    def __unicode__(self):
        return self.msisdn

    class Meta:
        verbose_name_plural = "Send Airtime"


class RequestAirtimeSend(models.Model):
    request_application = models.ForeignKey(AirtimeApplication,
                                            related_name="request_application")
    request_send_airtime = models.ForeignKey(SendAirtime,
                                             null=True,
                                             blank=True)
    msisdn = models.CharField(max_length=30,
                              verbose_name="MSISDN (Mobile Number)")
    product_key = models.CharField(max_length=10)
    amount  = models.IntegerField()
    sent = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True,
                                      blank=False,
                                      editable=False)

    def __unicode__(self):
        return self.msisdn

    class Meta:
        verbose_name_plural = "Request Airtime Send"


@receiver(post_save, sender=RequestAirtimeSend)
def send_random_airtime(sender, instance, signal, created, **kwargs):

    rand_int = randint(1, instance.request_application.ratio)

    if rand_int == 1:
        send_airtime = SendAirtime(app_id=instance.request_application,
                                   msisdn=instance.msisdn,
                                   product_key=instance.product_key,
                                   amount=instance.amount)
        send_airtime.save()

