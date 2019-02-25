from rest_framework import serializers
from .models import EvaluationTest


class EvaluationTestSerializer(serializers.ModelSerializer):
 class Meta:
  model = EvaluationTest
  fields='__all__'