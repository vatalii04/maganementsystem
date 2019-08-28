from django.urls import path
from . import views

urlpatterns = (
    path('', views.home, name='blog-home'),
    path('2/', views.contacts, name='blog-contacts'),
    path('4/', views.forum, name='blog-forum'),
)