from celery.decorators import task
from django.conf import settings
import requests
import json


@task
def send_bulk_sms(bulk_sms):
    """
    What if SMS is not sent?
    """
    data = {'objects' : bulk_sms}
    headers = {"content-type": "application/json"}
    url = "%s?username=%s&api_key=%s" % (settings.GOPHER_BASE_URL,
                                         settings.GOPHER_USERNAME,
                                         settings.GOPHER_API_KEY)
    response = requests.patch(url,
                              data=json.dumps(data),
                              headers=headers)
