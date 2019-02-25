from django.db import models
from users.models import User


class EvaluationTest(models.Model):
 title = models.CharField(max_length=50)
 admin = models.ForeignKey(User,on_delete=models.CASCADE)

 def __str__(self):
  return self.title


class GradeEvaluationText(models.Model):
 candidate = models.ForeignKey(User, on_delete=models.CASCADE)
 evaluationtest = models.ForeignKey(EvaluationTest,on_delete=models.SET_NULL,blank=True, null=True)
 grades=models.FloatField()
 def __str__(self):
  return self.candidate.username



class Choice(models.Model):
 title = models.CharField(max_length=50)
 def __str__(self):
  return self.title


class Question(models.Model):
 question = models.CharField(max_length=200)
 choices = models.ManyToManyField(Choice)
 answer = models.ForeignKey(Choice,on_delete=models.CASCADE,related_name='answer')
 evaluationtest = models.ForeignKey(EvaluationTest,on_delete=models.CASCADE)
 order =models.SmallIntegerField()

 def __str__(self):
  return self.question