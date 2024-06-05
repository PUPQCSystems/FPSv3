from django.db import models
from accounts.models import Faculty
# Create your models here.
class ServiceToTheCommunity(models.Model):
    extension_id = models.BigAutoField(primary_key=True)
    ext_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='extensionservices')
    activity = models.CharField(max_length=200)
    community = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_of_activity = models.CharField(max_length=50)
    hours_completed = models.CharField(max_length=10)
    extension_performance_score = models.IntegerField(default=0)
