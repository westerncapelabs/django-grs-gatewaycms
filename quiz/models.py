from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=20,
                            blank=False,
                            verbose_name="Name of Quiz")
    description = models.CharField(max_length=180)
    active = models.BooleanField()
    completed = models.BooleanField(editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    quiz_id = models.ForeignKey('Quiz',
                                related_name='quiz_ids')
    question = models.CharField(max_length=180, blank=False)

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = "Quiz Question"


class Answer(models.Model):
    # This class stores the answers.
    question_id = models.ForeignKey('Question',
                                    related_name="question_ids")
    answer = models.CharField(max_length=160)

    def __unicode__(self):
        return self.answer


class Response(models.Model):
    # This class stores the answers.
    question_id = models.ForeignKey('Question',
                                    related_name="question_ids")
    response = models.CharField(max_length=160)

    def __unicode__(self):
        return self.response


class FinalResponse(models.Model):
    quiz_id = models.ForeignKey('Quiz',
                                related_name='quiz_id')
    final_response = models.CharField(max_length=160)

    def __unicode__(self):
        return self.response
