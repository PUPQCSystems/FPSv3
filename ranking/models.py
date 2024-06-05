# Create your models here.
from django.db import models
# from evaluations.models import TeachingEffectiveness
# from extensionservices.models import ServiceToTheCommunity
# from prodevelopment.models import ContinuingDevelopment
# from research.models import PaperCounts
# from accounts.models import Faculty
# from decimal import Decimal

# class FacultyRanking(models.Model):
#     ranking_id = models.BigAutoField(primary_key=True)
#     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='ranking')
#     teaching_effectiveness = models.ForeignKey(TeachingEffectiveness, on_delete=models.CASCADE, related_name='rankings')
#     service_to_community = models.ForeignKey(ServiceToTheCommunity, on_delete=models.CASCADE, related_name='rankings')
#     continuing_development = models.ForeignKey(ContinuingDevelopment, on_delete=models.CASCADE, related_name='rankings')
#     research_paper = models.ForeignKey(PaperCounts, on_delete=models.CASCADE, related_name='rankings')
#     total_score = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # def calculate_total_score(self):
    #     teaching_score = self.teaching_effectiveness.eval_performance_score
    #     service_score = Decimal(self.service_to_community.extension_performance_score)
    #     development_score = Decimal(self.continuing_development.prodev_performance_score)
    #     research_score = Decimal(self.research_paper.research_performance_score)
    #     self.total_score = teaching_score + service_score + development_score + research_score
    
    # def save(self, *args, **kwargs):
    #     self.calculate_total_score()
    #     super().save(*args, **kwargs)