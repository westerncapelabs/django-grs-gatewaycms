from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    name = models.CharField(max_length=30,
                            blank=False,
                            verbose_name="Name of Quiz")
    description = models.CharField(max_length=180)
    active = models.BooleanField()
    updated_by = models.ForeignKey(User)
    updated_at = models.DateTimeField(auto_now_add=True,
                                      blank=False,
                                      editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    quiz_id = models.ForeignKey('Quiz',
                                related_name='q_quiz_id')
    question = models.CharField(max_length=163, blank=False)

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = "Quiz Question"


class Answer(models.Model):
    # This class stores the answers.
    question_id = models.ForeignKey('Question',
                                    related_name="question_id")
    answer = models.CharField(max_length=156)
    response = models.CharField(max_length=156)

    def __unicode__(self):
        return self.answer


class FinalResponse(models.Model):
    quiz_id = models.ForeignKey('Quiz',
                                related_name='fr_quiz_id')
    text = models.CharField(max_length=180)
    sms = models.CharField(max_length=160)
    for_total = models.IntegerField()

    def __unicode__(self):
        return self.text
