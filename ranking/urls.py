from django.urls import path
from . import views

app_name = 'ranking'

urlpatterns = [
    path('', views.ranking_views, name='ranking'),
]