from django.urls import path
from . import views


urlpatterns = (
    path('', views.home1, name='forum-home1'),
    path('3/', views.home2, name='forum-home2'),

)