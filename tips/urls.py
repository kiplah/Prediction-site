from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, PredictionViewSet

router = DefaultRouter()
router.register('matches', MatchViewSet)
router.register('predictions', PredictionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
