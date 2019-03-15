from django.db import models
from users.models import User
import re
from django.utils.translation import ugettext as _

# class CategoryManager(models.Manager):

#     def new_category(self, category):
#         new_category = self.create(category=re.sub('\s+', '-', category)
#                                    .lower())

#         new_category.save()
#         return new_category


class Category(models.Model):

    category = models.CharField(
        max_length=250, blank=True,
        unique=True, null=True)

    # objects = CategoryManager()

    def __str__(self):
        return self.category

class EvaluationTest(models.Model):
 title = models.CharField(max_length=50,blank=False)
 category=models.ForeignKey(Category,on_delete=models.CASCADE)
 admin = models.ForeignKey(User,on_delete=models.CASCADE)
 type = models.CharField(max_length=50)
                 
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
 answer = models.ForeignKey(Choice,on_delete=models.CASCADE,related_name='answer', blank=True, null=True)
 evaluationtest = models.ForeignKey(EvaluationTest,on_delete=models.CASCADE,related_name='questions', blank=True, null=True)
 order =models.SmallIntegerField()

 def __str__(self):
  return self.question

