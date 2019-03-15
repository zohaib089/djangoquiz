from api.views import CategoriesViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register(r'',CategoriesViewSet,base_name='categories')
urlpatterns=router.urls