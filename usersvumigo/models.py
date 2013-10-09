from django.db import models


class VumiGoUser(models.Model):
    msisdn = models.CharField(max_length=30,
                              blank=False,
                              verbose_name="MSISDN (Mobile Number)")
    sex = models.CharField(max_length=6)
    age = models.CharField(max_length=30)
    grade = models.CharField(max_length=3)
    community = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True,
                                      blank=False,
                                      editable=False)

    def __unicode__(self):
        return self.msisdn

    class Meta:
        verbose_name = "User"

class QuizResponse(models.Model):
    quiz = models.ForeignKey('quiz.Quiz',
                             verbose_name=u'Quiz')
    question = models.ForeignKey('quiz.Question',
                             verbose_name=u'Question')
    question_text = models.CharField(max_length=163, verbose_name=u'Question Text')
    correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(VumiGoUser,
                                    verbose_name=u'User')

    def __unicode__(self):
        return "%s" % self.question

    class Meta:
        verbose_name_plural = "Quiz Responses"
