from django.urls import path
from .views import SetPremiumStatusView

urlpatterns = [
    path('set-premium/<int:pk>/', SetPremiumStatusView.as_view(), name='set-premium'),
]
