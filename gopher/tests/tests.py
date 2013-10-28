# Python
import json

# Django
from django.core.urlresolvers import reverse

# Project
from gopher.models import AirtimeApplication, SendAirtime, RequestAirtimeSend

# Third Party
from tastypie.test import ResourceTestCase

class TestRequestRandom(ResourceTestCase):
    fixtures = ['test_random_gopher.json']

    def test_post_save_signal(self):
        app = AirtimeApplication.objects.get(name="test_application")
        airtime = RequestAirtimeSend(msisdn="27721231234",
                                     product_key="VOD",
                                     amount=500,
                                     sent=False,
                                     request_application=app)
        airtime.save()

        # Below works when the randomize value is off

        # send = SendAirtime.objects.get(msisdn="27721231234")
        # self.assertEqual(send.amount, 500)
        # self.assertEqual(send.msisdn, "27721231234")
        # self.assertEqual(send.product_key, "VOD")


    def test_api_exists(self):
        """
        Test base api name
        """
        url = reverse('api_dispatch_list',
                      kwargs={'resource_name': 'request/airtime',
                      'api_name': 'v1'})
        response = self.client.get(url)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(response.status_code, 200)
        json_item = json.loads(response.content)
        self.assertIn("meta", json_item)
        self.assertIn("objects", json_item)


    def test_api_sends(self):
        """
        Test base api name
        """
        url = reverse('api_dispatch_list',
                      kwargs={'resource_name': 'request/application',
                      'api_name': 'v1'})
        response = self.api_client.get("%s?name=test_application" % url)
        json_item = json.loads(response.content)
        app_uri = json_item['objects'][0]['resource_uri']

        url = reverse('api_dispatch_list',
                      kwargs={'resource_name': 'request/airtime',
                      'api_name': 'v1'})
        data = {"msisdn": "27721231239",
                "product_key": "VOD",
                "amount": 1000,
                "request_application": app_uri
        }

        for i in range(20):
            self.api_client.post(url,
                                    format="json",
                                    data=data)

        request = RequestAirtimeSend.objects.filter(msisdn="27721231239").all()
        self.assertEqual(len(request), 20)

        self.assertEqual(request[0].amount, 1000)
        self.assertEqual(request[0].msisdn, "27721231239")
        self.assertEqual(request[0].product_key, "VOD")

        send = SendAirtime.objects.filter(msisdn="27721231239").all()
        self.assertGreaterEqual(len(send), 4)
        self.assertLessEqual(len(send), 12)