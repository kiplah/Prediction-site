from rest_framework import generics, permissions
from .serializers import PremiumStatusSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class SetPremiumStatusView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PremiumStatusSerializer
    permission_classes = [permissions.IsAdminUser]
