from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from news.models import UserProfile, Publisher, Article

class Command(BaseCommand):
    help = 'Create demo data for the news app'

    def handle(self, *args, **options):
        # Clear all existing data first
        self.stdout.write('Clearing existing demo data...')
        Article.objects.all().delete()
        UserProfile.objects.all().delete()
        Publisher.objects.all().delete()
        
        # Delete only our demo users (be careful not to delete admin users)
        User.objects.filter(username__in=['reader', 'journalist', 'editor']).delete()

        self.stdout.write('Creating new demo data...')
        
        # Create users
        reader = User.objects.create_user('reader', 'reader@news.com', 'password123')
        journalist = User.objects.create_user('journalist', 'journalist@news.com', 'password123')
        editor = User.objects.create_user('editor', 'editor@news.com', 'password123')
        
        # Create profiles
        UserProfile.objects.create(user=reader, role='reader')
        UserProfile.objects.create(user=journalist, role='journalist')
        UserProfile.objects.create(user=editor, role='editor')
        
        # Create publisher
        news_pub = Publisher.objects.create(name='Daily News')
        news_pub.editors.add(editor)
        
        # Create sample articles with unique titles
        articles_data = [
            {
                'title': 'Welcome to Our News Platform',
                'content': 'This is the first article on our simple news platform...',
                'approved': True,
                'published': True
            },
            {
                'title': 'Technology Trends 2024',
                'content': 'Exploring the latest technology trends for 2024...',
                'approved': False,
                'published': False
            },
            {
                'title': 'Local Community Event',
                'content': 'Join us for the annual community festival this weekend...',
                'approved': True,
                'published': True
            },
            {
                'title': 'Health and Wellness Guide',
                'content': 'Tips for maintaining a healthy lifestyle...',
                'approved': False,
                'published': False
            },
            {
                'title': 'Sports Championship Results',
                'content': 'Final results from the regional sports championship...',
                'approved': True,
                'published': True
            }
        ]
        
        for article_data in articles_data:
            Article.objects.create(
                title=article_data['title'],
                content=article_data['content'],
                author=journalist,
                publisher=news_pub,
                is_approved=article_data['approved'],
                is_published=article_data['published']
            )
        
        self.stdout.write(self.style.SUCCESS('Demo data created successfully!'))
        self.stdout.write('Demo accounts:')
        self.stdout.write('- reader/password123')
        self.stdout.write('- journalist/password123')
        self.stdout.write('- editor/password123')