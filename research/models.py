from django.db import models
from accounts.models import Faculty
# Create your models here.
class PaperCounts(models.Model):
    research_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='research')
    title = models.CharField(max_length=300)
    output_type = models.CharField(max_length=50)
    journal_publisher = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    date_published = models.CharField(max_length=50)
    year_published = models.CharField(max_length=4)
    research_performance_score = models.IntegerField(default=0) 