from rest_framework import viewsets
from .models import EvaluationTest
from .serializers import EvaluationTestSerializer



class EvaluationTestViewSet(viewsets.ModelViewSet):
 serializer_class = EvaluationTestSerializer
 queryset = EvaluationTest.objects.all()