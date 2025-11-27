from django.db import models
from django.contrib.auth.models import User

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    editors = models.ManyToManyField(User, related_name='publisher_editors')
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('reader', 'Reader'),
        ('journalist', 'Journalist'),
        ('editor', 'Editor'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='reader')
    subscribed_publishers = models.ManyToManyField(Publisher, blank=True)
    subscribed_journalists = models.ManyToManyField(User, blank=True, related_name='subscribers')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"