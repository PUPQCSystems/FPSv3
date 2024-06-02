from django.urls import path
from . import views

app_name = 'extensionservices'

urlpatterns = [
    path('', views.extension_views, name='extension'),
]