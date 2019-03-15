from rest_framework.routers import DefaultRouter
from api.views import EvaluationTestViewSet


router = DefaultRouter()
router.register(r'',EvaluationTestViewSet,base_name='evaluationtest'),
urlpatterns=router.urls