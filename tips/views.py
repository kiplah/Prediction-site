from rest_framework import viewsets, permissions
from .models import Match, Prediction
from ..users.serializers import MatchSerializer, PredictionSerializer
from django_filters.rest_framework import DjangoFilterBackend

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
class PredictionViewSet(viewsets.ModelViewSet):
    ...
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'match__match_date': ['gte', 'lte'],
        'match__league': ['exact', 'icontains'],
        'is_premium': ['exact']
    }
