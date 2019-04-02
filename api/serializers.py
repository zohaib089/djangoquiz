from rest_framework import serializers
from .models import EvaluationTest, Question, Choice, GradeEvaluationText, Category
from users.models import User


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class QuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'choices', 'question', 'order')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EvaluationTestSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    admin = StringSerializer(many=False)
    category = StringSerializer(many=False)

    class Meta:
        model = EvaluationTest
        fields = '__all__'

    def get_questions(self, obj):
        questions = QuestionSerializer(obj.questions.all(), many=True).data
        return questions

    def create(self, request):
        data = request.data
        print(data)
        evaluationtest = EvaluationTest()
        admin = User.objects.get(username=data['admin'])
        cat = Category.objects.get(id=data['category'])
        print(cat)
        evaluationtest.category = cat
        evaluationtest.admin = admin
        evaluationtest.title = data['title']
        evaluationtest.type = data['type']
        evaluationtest.save()

        order = 1
        for q in data['questions']:
            newQ = Question()
            newQ.question = q['title']
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

    def update(self, instance, validated_data):
        # recupero i dati dalla request
        data = self.context['request'].data
        instance = EvaluationTest()
        # admin non necessario, genera errore perchè il numero degli argomenti restituiti non
        # corrisponde a quelli richiesti
        admin = User.objects.get(username=data['admin'])
        questions = QuestionSerializer()
        # choices = StringSerializer()
        # utilizzo il valore di category(recuperato dalla request) per aggiornare la categoria associata
        cat = Category.objects.get(id=data['category'])

        instance.category = cat

        instance.category = validated_data.get('id', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.type = validated_data.get('type', instance.type)
        instance.admin = admin
        instance.save()

        #  instance = evaluationtest()
        keep_questions = []
        for question in questions:
            if "id" in questions:
                if Question.objects.filter(id=questions["id"]).exists():
                    q = Question.objects.get(id=questions["id"])
                    q.question = question.get('question', q.question)
                    q.save()
                else:
                    continue
            # else:
            #     q = Question.objects.create(
            #         **questions, evaluationtest=instance)
                keep_questions.append(q.id)
        # for question in instance.questions:
        #     if question.id not in keep_questions:
        #         question.delete()
            keep_choices = []
            for choice in choices:
                if "id" in choice.keys():
                    if Choice.objects.filter(id=choice["id"]).exists():
                        c = Choice.objects.get(id=choice["id"])
                        c.title = choice.get('title', c.title)
                        c.save()
                    else:
                        continue
                else:
                    c = Choice.objects.create(
                        **choice, evaluationtest=instance)
                    keep_choices.append(c.id)
            for choice in instance.choices:
                if choice.id not in keep_choices:
                    choice.delete()

        #  order = 1
        #  for q in instance['questions']:
        #    newQ = Question()
        #    newQ.question=q['title']
        #    newQ.order = order
        #    newQ.save()

        #    for c in q['choices']:
        #      newC = Choice()
        #      newC.title = c
        #      newC.save()
        #      newQ.choices.add(newC)
        #    newQ.answer = Choice.objects.get(title=q['answer'])
        #    newQ.instance = instance
        #    newQ.save()
        #    order += 1
        return instance


class GradeEvaluationTextSerializer(serializers.ModelSerializer):
    candidate = StringSerializer(many=False)

    class Meta:
        model = GradeEvaluationText
        fields = ('__all__')

    def create(self, request):
        data = request.data
        print(data)
        evaluationtest = EvaluationTest.objects.get(id=data['testId'])
        candidate = User.objects.get(username=data['username'])

        graded_test = GradeEvaluationText()
        graded_test.evaluationtest = evaluationtest
        graded_test.candidate = candidate

        questions = [q for q in evaluationtest.questions.all()]
        answers = [data['answers'][a] for a in data['answers']]

        answered_correct_count = 0

        for i in range(len(questions)):
            if questions[i].answer.title == answers[i]:
                answered_correct_count += 1
            i += 1
        grades = answered_correct_count/len(questions)*100
        graded_test.grades = grades
        graded_test.save()
        return graded_test
     