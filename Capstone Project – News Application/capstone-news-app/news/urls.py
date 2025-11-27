from django.urls import path
from . import views

urlpatterns = [
    path('approve/<int:article_id>/', views.approve_article, name='approve_article'),
    path('logout/', views.custom_logout, name='logout'),
]