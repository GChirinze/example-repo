from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from news import views as news_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', news_views.dashboard, name='dashboard'),
    path('articles/', news_views.articles, name='articles'),
    path('news/', include('news.urls')),
]