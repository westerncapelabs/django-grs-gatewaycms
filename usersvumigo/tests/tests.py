from tastypie.test import ResourceTestCase
from django.core.urlresolvers import reverse
import json
from usersvumigo.models import VumiGoUser
import datetime


class SimpleTest(ResourceTestCase):
    def test_basic_api_functionality(self):
        """
            Testing basic API functionality.
        """
        url = reverse('api_dispatch_list',
                      kwargs={'resource_name': 'users',
                      'api_name': 'v1'})
        response = self.client.get(url)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(response.status_code, 200)
        json_item = json.loads(response.content)
        self.assertIn("meta", json_item)
        self.assertIn("objects", json_item)

    def test_post_registration_good_data(self):
        """
            Testing Registration.
        """
        url = reverse('api_dispatch_list',
                      kwargs={'resource_name': 'users',
                      'api_name': 'v1'})
        response = self.api_client.post(url,
                                    format="json",
                                    data={"sex": "female",
                                    "msisdn": "0723456789",
                                    "age": "16 or older",
                                    "community": "Meadowlands"
                                    })

        json_item = json.loads(response.content)
        self.assertEqual("female", json_item["sex"])
        self.assertEqual("0723456789", json_item["msisdn"])
        self.assertEqual("16 or older", json_item["age"])
        self.assertEqual("Meadowlands", json_item["community"])
