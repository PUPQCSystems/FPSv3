from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.manangement_views, name='management'),
]