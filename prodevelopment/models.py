from django.db import models
from accounts.models import Faculty
# Create your models here.
class ContinuingDevelopment(models.Model):
    prodev_id = models.BigAutoField(primary_key=True)
    participant = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='prodevelopment')
    event = models.CharField(max_length=200)
    organizer = models.CharField(max_length=100)
    scope = models.CharField(max_length=50)
    hrs_accumulated = models.CharField(max_length=50)
    event_date = models.CharField(max_length=50)
    prodev_performance_score = models.IntegerField(default=0)