from api.views import GradedAssignmentListView,GradeEvaluationTextCreateView
from django.urls import path

urlpatterns=[
 path('',GradedAssignmentListView.as_view()),
 path('create/',GradeEvaluationTextCreateView.as_view())
]