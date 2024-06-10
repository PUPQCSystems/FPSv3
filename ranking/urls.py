from django.urls import path
from . import views

app_name = 'ranking'

urlpatterns = [
    path('', views.ranking_views, name='ranking'),
    path('ranking/', views.ranking_tableview, name='ranking_table'),
    path('post-faculty-rank/', views.POST_facultyname, name='post_faculty_rank'),
    path('get_faculty_rank/', views.GET_facultynewrank, name='get_faculty_rank'),
    path('edit_rank_evaluation/', views.POST_rankingtable, name='edit_rank_evaluation'),
]