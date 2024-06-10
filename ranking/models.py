# Create your models here.
from django.db import models
from accounts.models import Faculty

class FacultyRankEvaluations(models.Model):
    rank_id = models.BigAutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='ranking')
    current_rank = models.CharField(max_length=50, null=True, blank=True)
    kra_one_pts = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)
    kra_two_pts = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)
    kra_three_pts = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)
    kra_four_pts = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)
    grandtotal_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)
    rank_bracket_count = models.IntegerField(default=0, null=True, blank=True)
    new_rank = models.CharField(max_length=50, null=True, blank=True)
    impression = models.CharField(max_length=50, null=True, blank=True)
    auto_rank = models.BooleanField(default=False)
    rank_eval_date = models.DateTimeField()