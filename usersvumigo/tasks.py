from celery.decorators import task
from django.conf import settings
import requests
import json


@task
def send_bulk_sms(bulk_sms):
    print "sending bulk sms"
    data = {'objects' : bulk_sms}
    headers = {"content-type": "application/json"}
    response = requests.patch(settings.GOPHER_BASE_URL, data=json.dumps(data), headers=headers)
