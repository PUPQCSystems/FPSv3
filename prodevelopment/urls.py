from django.urls import path
from . import views

app_name = 'prodevelopment'

urlpatterns = [
    path('', views.prodev_views, name='prodevelopment'),
]