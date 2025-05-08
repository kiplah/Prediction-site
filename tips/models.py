from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Match(models.Model):
    league = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.league})"

class Prediction(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='predictions')
    predicted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    prediction_text = models.TextField()
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.match}"
