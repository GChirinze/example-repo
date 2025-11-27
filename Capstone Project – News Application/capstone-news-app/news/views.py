from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from .models import Article, Publisher, UserProfile
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
def home(request):
    recent_articles = Article.objects.filter(is_published=True).order_by('-created_at')[:5]
    return render(request, 'home.html', {'articles': recent_articles})

@login_required
def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    articles = Article.objects.all()
    
    if user_profile.role == 'reader':
        articles = articles.filter(is_published=True)
    elif user_profile.role == 'journalist':
        articles = articles.filter(author=request.user)
    
    return render(request, 'dashboard.html', {
        'profile': user_profile,
        'articles': articles
    })

@login_required
def articles(request):
    published_articles = Article.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'articles.html', {'articles': published_articles})

def is_editor(user):
    try:
        profile = UserProfile.objects.get(user=user)
        return profile.role == 'editor'
    except UserProfile.DoesNotExist:
        return False

@login_required
@user_passes_test(is_editor)
def approve_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.is_approved = True
    article.is_published = True
    article.save()
    messages.success(request, f'Article "{article.title}" has been approved and published!')
    return redirect('dashboard')




def custom_logout(request):
    if request.user.is_authenticated:
        messages.info(request, f'You have been logged out successfully. Goodbye, {request.user.username}!')
    logout(request)
    return redirect('home')
