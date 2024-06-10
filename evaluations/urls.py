from django.urls import path
from . import views

app_name = 'evaluations'

urlpatterns = [
    path('', views.evaluations_view, name='evaluations'),
    path('evaluations/', views.eval_table_view, name='eval_table'),
    path('get_table/', views.GET_evaltable, name='get_table'),
]