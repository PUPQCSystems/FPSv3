from django.db import models
from accounts.models import Faculty
# Create your models here.
class TeachingEffectiveness(models.Model):
    evaluations_id = models.BigAutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='evaluations')
    semesters = models.CharField(max_length=10)
    academic_yr = models.CharField(max_length=50)
    student_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    sr_interpretation = models.CharField(max_length=50)
    supervisor_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    sp_interpretation = models.CharField(max_length=50)
    average_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ar_interpretation = models.CharField(max_length=50)
    eval_performance_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)