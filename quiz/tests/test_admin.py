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
                         'answers-0-response': "R1",
                         "answers-0-correct": True
                         })

        query = Quiz.objects.get(name="Quiz Test Title")
        question = query.questions.all()[0]
        answer = question.answers.all()[0]
        self.assertEqual(question.question, "This is the first QUestion?")
        self.assertEqual(answer.answer, "Yes")
        self.assertEqual(answer.response, "R1")
        self.assertEqual(answer.correct, True)

    def test_admin_no_correct_answers(self):
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
        response = self.client.post(url, data={"question": "This is the first QUestion?",
                                    "quiz_id": query.id,
                                    "answers-INITIAL_FORMS": 0,
                                    'answers-TOTAL_FORMS': 5,
                                    'answers-MAX_NUM_FORMS':  u'',
                                    "answers-0-answer": "Yes",
                                    'answers-0-response': "R1",
                                 })

        self.assertIn("You need only one correct answer",
                      response.context_data["errors"])

    def test_admin_multiple_correct_answers(self):
        """
        Testing multipe correct answers
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
        response = self.client.post(url, data={"question": "This is the first QUestion?",
                                    "quiz_id": query.id,
                                    "answers-INITIAL_FORMS": 0,
                                    'answers-TOTAL_FORMS': 5,
                                    'answers-MAX_NUM_FORMS':  u'',
                                    "answers-0-answer": "Yes",
                                    'answers-0-response': "R1",
                                    "answers-0-correct": True,
                                    "answers-1-answer": "Nonsense",
                                    'answers-1-response': "R2",
                                    "answers-1-correct": True
                                 })

        self.assertIn("You need only one correct answer",
                      response.context_data["errors"])

    def test_admin_quiz_exceed_limit(self):
        """
        Test to see if quiz exceeds limit
        """
        self.client.login(username=self.admin.username,
                          password="pass123")

        url = reverse("admin:quiz_quiz_add")
        self.client.post(url, data={"name": "Quiz Test Title",
                         "description": "Quiz Test Description"})
        query = Quiz.objects.get(name="Quiz Test Title")

        url = reverse("admin:quiz_question_add")
        response = self.client.post(url, data={"question": ("Lorem ipsum dolor sit amet",
                                    "consectetur adipisicing elit. Enim segnitiae?"),
                                    "quiz_id": query.id,
                                    "answers-INITIAL_FORMS": 0,
                                    'answers-TOTAL_FORMS': 5,
                                    'answers-MAX_NUM_FORMS': u'',
                                    "answers-0-answer": ("Lorem ipsum dolor sit amet,"
                                                         "consectetur adipisicing elit. Nobis, meque romanum."),
                                    'answers-0-response': "R1",
                                    "answers-1-answer": "Lorem ipsum dolor sit amet, consectetur adipisicing.",
                                    'answers-1-response': "R1"
                                     })

        self.assertIn("You have gone beyond the character limit please shorten questions and/or answers",
                      response.context_data["errors"])
