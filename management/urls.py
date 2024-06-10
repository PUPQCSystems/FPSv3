from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.manangement_views, name='management'),
    path('management/', views.GET_rankingtable, name='get_reports'),
    path('export/', views.POST_export, name='export'),
]