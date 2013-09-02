from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from quiz.models import (Quiz, Question, Answer, FinalResponse)
from django.utils import timezone


class TestAdminView(TestCase):
    """
    Testing Super User
    """
    fixtures = ['quiz_sample.json']
    def setUp(self):
        self.admin = User.objects.create_superuser('admin',
                                                    'admin@test.com', 
                                                    'pass123')

    def test_admin_view(self):
        self.client.login(username=self.admin.username,
                          password="pass123")

        url_index = reverse("admin:index")
        response = self.client.get(url_index)
        # import pdb; pdb.set_trace()
        # index_result = response.__dict__['context_data']['cl'].__dict__['result_list']
        # print index_result

        url = reverse("admin:quiz_quiz_changelist")
        response = self.client.get(url)
        quiz_result = response.__dict__['context_data']['cl'].__dict__['result_list']
        quizzes = []
        [quizzes.append(q.name) for q in quiz_result]
        self.assertEqual(sorted(quizzes), sorted(["Quiz Welcome"]))


    def test_admin_create_quiz(self):
        """
        Testing Creating a Quiz
        """
        self.client.login(username=self.admin.username,
                          password="pass123")

        time = timezone.now()
        url = reverse("admin:quiz_quiz_add")
        self.client.post(url, data={"name": "Quiz Test Title",
                         "description": "Quiz Test Description"})
        query = Quiz.objects.get(name="Quiz Test Title")
        self.assertEqual(query.name, "Quiz Test Title")
        self.assertEqual(query.updated_by, self.admin)
        self.assertGreater(query.updated_at, time)


        url = reverse("admin:quiz_question_add")
        self.client.post(url, data={"question": "This is the first QUestion?",
                         "quiz_id": query.id,
                         "answers-INITIAL_FORMS": 0,
                         'answers-TOTAL_FORMS': 5,
                         'answers-MAX_NUM_FORMS':  u'',
                         "answers-0-answer": "Yes",
                         'answers-0-response': "R1"
                         })

        query = Quiz.objects.get(name="Quiz Test Title")
        question = query.questions.all()[0]
        answer = question.answers.all()[0]
        self.assertEqual(question.question, "This is the first QUestion?")
        self.assertEqual(answer.answer, "Yes")
        self.assertEqual(answer.response, "R1")
