from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
 HTTP_201_CREATED,
 HTTP_400_BAD_REQUEST
)
from .models import EvaluationTest,GradeEvaluationText,Category
from .serializers import EvaluationTestSerializer,GradeEvaluationTextSerializer,CategorySerializer
from rest_framework.generics import ListAPIView,CreateAPIView


class EvaluationTestViewSet(viewsets.ModelViewSet):
 
 permission_classes = (IsAuthenticated, )
 serializer_class = EvaluationTestSerializer
 queryset = EvaluationTest.objects.all()
 
 def create(self,request):
  serializer = EvaluationTestSerializer(data=request.data)
  if serializer.is_valid():
   evaluationtest = serializer.create(request)
   print(evaluationtest)
   if evaluationtest:
    return Response(status = HTTP_201_CREATED)
  return Response(status = HTTP_400_BAD_REQUEST)
class GradedAssignmentListView(ListAPIView):
  serializer_class= GradeEvaluationTextSerializer


  def get_queryset(self):
      queryset = GradeEvaluationText.objects.all()
      username = self.request.query_params.get('username',None)

      if username is not None:
        queryset = queryset.filter(candidate__username=username)
      return queryset  
class CategoriesViewSet(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()
  # permission_classes = (IsAuthenticated)
  #                         # IsOwnerOrReadOnly,)
  def perform_create(self, serializer):
        serializer.save()

class GradeEvaluationTextCreateView(CreateAPIView):
  serializer_class = GradeEvaluationTextSerializer
  queryset = GradeEvaluationText.objects.all()

  def post(self,request):
    print(request.data)
    serializer = GradeEvaluationTextSerializer(data=request.data)
    serializer.is_valid()
    GradeEvaluationText = serializer.create(request)
    if GradeEvaluationText:
       return Response(status = HTTP_201_CREATED)
    return Response(status = HTTP_400_BAD_REQUEST)