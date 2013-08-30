from tastypie.test import ResourceTestCase
from django.core.urlresolvers import reverse
import json
from quiz.models import (Quiz, Question, Answer, FinalResponse)


class TestQuizApi(ResourceTestCase):
    fixtures = ['user_test.json', 'quiz_test.json']

    def test_fixtures_loaded(self):
        query = Quiz.objects.all()
        x = []
        [x.append(obj.name) for obj in query]
        self.assertEqual(sorted(x),
                         sorted(["quiz one", "quiz two", "quiz three"]))

    def test_quiz_object_list(self):
        """
        Testing returning the object list
        """
        url = reverse('api_dispatch_list',
                      kwargs={'resource_name': 'quiz',
                      'api_name': 'v1'})
        response = self.client.get(url)
        self.assertEqual("application/json", response["Content-Type"])
        self.assertEqual(response.status_code, 200)
        json_item = json.loads(response.content)
        self.assertIn("meta", json_item)
        self.assertIn("objects", json_item)
        [self.assertTrue(obj["active"]) for obj in json_item["objects"]]
