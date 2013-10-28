from gopher.models import AirtimeApplication, SendAirtime, RequestAirtimeSend
from django.core.urlresolvers import reverse
from tastypie.test import ResourceTestCase


class TestRequestRandom(ResourceTestCase):
    def test_post_save_signal(self):
        airtime = RequestAirtimeSend(msisdn="27721231234",
                                     product_key="VOD",
                                     amount=500,
                                     sent=False)
        airtime.save()

        send = SendAirtime.objects.get(msisdn="27721231234")
        self.assertEqual(send, 500)

    def test_api_sends(self):
        pass

    def test_random_airtime_added_on_api(self):
        pass