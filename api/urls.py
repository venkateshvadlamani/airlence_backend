from django.urls import path

from api.views import SignupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', SignupViewSet, base_name='signup')
urlpatterns = router.urls
