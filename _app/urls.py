"""
URL configuration for _app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve

from _app import views

# Correct assignment of handlers to view functions
handler500 = views.error_500view
handler404 = views.error_404view
handler403 = views.error_403view
handler400 = views.error_400view

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('', views.accounts_login, name='login'),
    path('logout/', views.account_logout, name='logout'),

    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('evaluations/', include('evaluations.urls', namespace='evaluations')),
    path('management/', include('management.urls', namespace='management')),
    path('prodevelopment/', include('prodevelopment.urls', namespace='prodevelopment')),
    path('ranking/', include('ranking.urls', namespace='ranking')),
    path('research/', include('research.urls', namespace='research')),
    path('extension/', include('extensionservices.urls', namespace='extension')),
    
    path('license/', views.license, name='license'),
    path('documentation/', views.documentation, name='documentation'),
] + staticfiles_urlpatterns()
