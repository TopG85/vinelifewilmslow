from django.core.management.base import BaseCommand
from wagtail.models import Page
from core.models import (
    HomePage, MissionPage, LeadershipPage, WorshipPage,
    GroupsPage, ResourcesPage, ContactPage, YouTubePage, NotificationPage
)


class Command(BaseCommand):
    help = 'Create all Vinelife editable pages'

    def handle(self, *args, **options):
        root = Page.get_first_root_node()
        
        # Check if pages already exist
        existing = root.get_children().count()
        if existing > 0:
            self.stdout.write(self.style.WARNING(f'⚠️  Root already has {existing} children. Skipping.'))
            return
        
        pages_to_create = [
            {
                'model': HomePage,
                'data': {
                    'title': 'Home',
                    'slug': 'home',
                    'hero_title': 'Welcome to Vinelife Wilmslow',
                    'hero_subtitle': 'A community church in Wilmslow, Cheshire',
                    'hero_cta_text': 'Learn More',
                    'hero_cta_url': '/mission/',
                    'facebook_url': 'https://www.facebook.com/vinelifewilmslow'
                }
            },
            {
                'model': MissionPage,
                'data': {
                    'title': 'Our Mission',
                    'slug': 'mission',
                    'main_content': '<p>Vinelife Wilmslow: spreading the Gospel and serving our community</p>'
                }
            },
            {
                'model': LeadershipPage,
                'data': {
                    'title': 'Leadership',
                    'slug': 'leadership',
                    'intro': '<p>Meet our leaders</p>'
                }
            },
            {
                'model': WorshipPage,
                'data': {
                    'title': 'Worship & Services',
                    'slug': 'worship',
                    'intro': '<p>Sunday worship services</p>'
                }
            },
            {
                'model': GroupsPage,
                'data': {
                    'title': 'Groups',
                    'slug': 'groups',
                    'intro': '<p>Connect with our groups</p>'
                }
            },
            {
                'model': ResourcesPage,
                'data': {
                    'title': 'Local Resources',
                    'slug': 'resources',
                    'intro': '<p>Community resources</p>'
                }
            },
            {
                'model': ContactPage,
                'data': {
                    'title': 'Contact Us',
                    'slug': 'contact',
                    'intro': '<p>Get in touch</p>',
                    'email': 'info@vinelifewilmslow.com',
                    'phone': '+44 (0) 1625 525000',
                    'address': 'The Open Arms Youth Project, Howty Close, Wilmslow'
                }
            },
            {
                'model': YouTubePage,
                'data': {
                    'title': 'YouTube',
                    'slug': 'youtube',
                    'channel_url': 'https://www.youtube.com/channel/UC0G20x3mVQwmqGUAig_MAcA',
                    'description': '<p>Watch our videos</p>'
                }
            },
            {
                'model': NotificationPage,
                'data': {
                    'title': 'Thought for the Day',
                    'slug': 'thought',
                    'current_message': '<p>Daily inspiration</p>',
                    'author': 'Vinelife Team'
                }
            }
        ]
        
        for page_config in pages_to_create:
            model = page_config['model']
            data = page_config['data']
            page = model(**data)
            root.add_child(instance=page)
            page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS(f'✅ Created: {page.title}'))
        
        self.stdout.write(self.style.SUCCESS('\n🎉 All pages created and published!'))
