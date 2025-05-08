from rest_framework import serializers
from .models import Match, Prediction

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    match = MatchSerializer(read_only=True)

    class Meta:
        model = Prediction
        fields = '__all__'
