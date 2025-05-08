from rest_framework import viewsets, permissions
from .models import Match, Prediction
from .serializers import MatchSerializer, PredictionSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all().order_by('-match_date')
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all().order_by('-created_at')
    serializer_class = PredictionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and getattr(user, 'is_premium', False):
            return self.queryset
        return self.queryset.filter(is_premium=False)
