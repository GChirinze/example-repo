from django.contrib import admin
from .models import Article, Publisher, UserProfile

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_approved', 'is_published', 'created_at']
    list_filter = ['is_approved', 'is_published', 'created_at']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
