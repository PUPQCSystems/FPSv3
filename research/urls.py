from django.urls import path
from . import views

app_name = 'research'

urlpatterns = [
    path('', views.research_views, name='research'),
    path('research/', views.research_table_view, name='research_table'),
]