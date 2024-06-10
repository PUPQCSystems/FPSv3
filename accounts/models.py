from django.db import models

# Create your models here.
class Faculty(models.Model):
    faculty_id = models.BigAutoField(primary_key=True)
    faculty_name = models.CharField(max_length=100)
    faculty_type = models.CharField(max_length=50)
    faculty_rank = models.CharField(max_length=50)
