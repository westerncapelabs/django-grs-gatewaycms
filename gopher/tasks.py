from gopher.models import SendAirtime
from celery.decorators import task
from celery.utils.log import get_task_logger
from django.conf import settings
import requests
import json

logger = get_task_logger(__name__)


@task
def get_new_recharge():
    print "Running celery beat"
    logger.info("Checking for new recharges")
    queryset = SendAirtime.objects.filter(sent=False)
    bulk_sms = [{"msisdn": obj.msisdn, "denomination": obj.amount, "product_code": obj.product_key} for obj in queryset.all()]
    if bulk_sms:
        send_bulk_sms.delay(bulk_sms)
        queryset.update(sent=True)


@task
def send_bulk_sms(bulk_sms):
    """
    What if SMS is not sent?
    """
    logger.info("Got bulk recharges now doing the updates")
    data = {'objects' : bulk_sms}
    headers = {"content-type": "application/json"}
    url = "%s?username=%s&api_key=%s" % (settings.GOPHER_BASE_URL,
                                         settings.GOPHER_USERNAME,
                                         settings.GOPHER_API_KEY)
    response = requests.patch(url,
                              data=json.dumps(data),
                              headers=headers)
