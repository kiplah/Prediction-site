from rest_framework import serializers
from .models import Match, Prediction
from django.contrib.auth import get_user_model

User = get_user_model()

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    match = MatchSerializer(read_only=True)

    class Meta:
        model = Prediction
        fields = '__all__'
class PremiumStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_premium']
        read_only_fields = ['id', 'email']