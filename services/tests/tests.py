from tastypie.test import ResourceTestCase
from django.core.urlresolvers import reverse
import json
from services.models import Service
import datetime


class TestService(ResourceTestCase):
    def test_basic_api_functionality(self):
        """
            Testing basic API functionality.
        """
        url = reverse('api_dispatch_list',
                      kwargs={'resource_name': 'category',
                      'api_name': 'v1'})
        response = self.client.get(url)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(response.status_code, 200)
        json_item = json.loads(response.content)
        self.assertIn("meta", json_item)
        self.assertIn("objects", json_item)
