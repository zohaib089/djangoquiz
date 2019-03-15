from rest_framework import serializers
from .models import EvaluationTest,Question,Choice,GradeEvaluationText,Category
from users.models import User


class StringSerializer(serializers.StringRelatedField):
 def to_internal_value(self,value):
  return value

class QuestionSerializer(serializers.ModelSerializer):
 choices = StringSerializer(many=True)
 class Meta:
  model = Question
  fields = ('id','choices','question','order')

class CategorySerializer(serializers.ModelSerializer):
 class Meta:
    model = Category
    fields='__all__'

    
class EvaluationTestSerializer(serializers.ModelSerializer):
 questions = serializers.SerializerMethodField()
 admin = StringSerializer(many=False)
 category = StringSerializer(many=False)
 class Meta:
  model = EvaluationTest
  fields='__all__'

 def get_questions(self,obj):
  questions = QuestionSerializer(obj.questions.all(), many=True).data
  return questions

 def create(self,request):
   data = request.data
   print(data)
   evaluationtest = EvaluationTest()
   admin= User.objects.get(username=data['admin'])
   cat=Category.objects.get(id=data['category'])
   print(cat)
   evaluationtest.category=cat
   evaluationtest.admin = admin
   evaluationtest.title = data['title']
   evaluationtest.type = data['type']
   evaluationtest.save()
   
   order = 1
   for q in data['questions']:
     newQ = Question()
     newQ.question=q['title']
     newQ.order = order
     newQ.save()

     for c in q['choices']:
       newC = Choice()
       newC.title = c
       newC.save()
       newQ.choices.add(newC)
     newQ.answer = Choice.objects.get(title=q['answer'])
     newQ.evaluationtest = evaluationtest
     newQ.save()
     order += 1
   return evaluationtest

#  def update(self,instance,validated_data):
#   #  data = request.data
#   #  print(data)
#   #  evaluationtest = EvaluationTest()
#   #  admin= User.objects.get('username')
#   #  cat=Category.objects.get('id')
#   #  print(cat)
#   #  instance.category=cat
    
#    instance.category = validated_data.get('id',instance.category)
#    instance.title = validated_data.get('title',instance.title)
#    instance.type = validated_data.get('type',instance.type)
#    instance.save()

#    instance = EvaluationTest()
#   #  keep_questions=[]
#   #  existing_id=[q.id for q in instance.questions]
#    order = 1
#    for q in instance['questions']:
#      newQ = Question()
#      newQ.question=q['title']
#      newQ.order = order
#      newQ.save()

#      for c in q['choices']:
#        newC = Choice()
#        newC.title = c
#        newC.save()
#        newQ.choices.add(newC)
#      newQ.answer = Choice.objects.get(title=q['answer'])
#      newQ.instance = instance
#      newQ.save()
#      order += 1
#    return instance


   
class GradeEvaluationTextSerializer(serializers.ModelSerializer):
  candidate = StringSerializer(many=False)
  class Meta:
    model = GradeEvaluationText
    fields=('__all__')
  def create(self,request):
    data = request.data
    print(data)
    evaluationtest = EvaluationTest.objects.get(id=data['testId'])
    candidate = User.objects.get(username=data['username'])

    graded_test = GradeEvaluationText()
    graded_test.evaluationtest = evaluationtest
    graded_test.candidate =  candidate

    questions = [q for q in evaluationtest.questions.all()]
    answers = [data['answers'][a] for a in data['answers']]
     
    answered_correct_count = 0

    for i in range(len(questions)):
      if questions[i].answer.title == answers[i]:
         answered_correct_count +=1
      i +=1
    grades = answered_correct_count/len(questions)*100
    graded_test.grades = grades
    graded_test.save()
    return graded_test
     