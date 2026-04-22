from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    TabbedInterface, ObjectList, FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)


class HomePage(Page):
    """Complete home page with all sections (Hero, Mission, Founders, etc.)"""
    # Hero Section
    hero_image_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="First hero background image"
    )
    hero_image_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Second hero background image"
    )
    hero_title = models.CharField(max_length=255, blank=True, default="Vinelife Church Wilmslow")
    hero_cta_1_label = models.CharField(max_length=100, blank=True, default="Our Mission")
    hero_cta_1_link = models.CharField(max_length=100, blank=True, default="#about")
    hero_cta_2_label = models.CharField(max_length=100, blank=True, default="Get In Touch")
    hero_cta_2_link = models.CharField(max_length=100, blank=True, default="#contact")
    facebook_url = models.URLField(blank=True, default='https://www.facebook.com/VinelifeChurchWilmslow')
    # Mission Section
    mission_title = models.CharField(max_length=255, blank=True, default="Our Mission")
    mission_content = RichTextField(blank=True)
    mission_readmore_label = models.CharField(max_length=100, blank=True, default="Read More")
    mission_history_title = models.CharField(max_length=255, blank=True, default="History")
    mission_history = RichTextField(blank=True)
    # Founders Section
    founders_title = models.CharField(max_length=255, blank=True, default="Founders")
    founders_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Founders photo"
    )
    founders_caption = models.CharField(max_length=255, blank=True, default="Robert & Cheryl Larkman - Founders of Vinelife Church")
    founders_content = RichTextField(blank=True)
    # Thought for Day
    thought_title = models.CharField(max_length=255, blank=True, default="Thought for the Day")
    # Worship/Events
    worship_title = models.CharField(max_length=255, blank=True, default="Sunday Worship Meetings")
    worship_subtitle = models.CharField(max_length=255, blank=True, default="Stay connected with what's happening at Vinelife Wilmslow")
    # Special Events
    special_events_title = models.CharField(max_length=255, blank=True, default="Special Events")
    special_events_subtitle = models.CharField(max_length=255, blank=True)
    # Groups
    groups_title = models.CharField(max_length=255, blank=True, default="Groups at Vinelife Church")
    groups_subtitle = models.CharField(max_length=255, blank=True, default="We have groups for men & women.")
    mens_group_title = models.CharField(max_length=100, blank=True, default="Men's Group")
    mens_group_description = RichTextField(blank=True)
    mens_group_meetings = models.CharField(max_length=255, blank=True, default="First and third Mondays of each month evening")
    mens_group_contact = models.CharField(max_length=20, blank=True, default="07957 813360")
    womens_group_title = models.CharField(max_length=100, blank=True, default="Women's Group")
    womens_group_description = RichTextField(blank=True)
    womens_group_meetings = models.CharField(max_length=255, blank=True, default="First and third Mondays of each month (morning and evening)")
    womens_group_contact = models.CharField(max_length=20, blank=True, default="07942 876042")

    # YouTube Section
    youtube_channel_title = models.CharField(max_length=255, blank=True, default="YouTube Channel")
    youtube_embed_url = models.URLField(blank=True, help_text="YouTube embed URL (e.g. https://www.youtube.com/embed/VIDEO_ID)")
    youtube_url = models.URLField(blank=True, help_text="YouTube channel link")
    
    # Media Library Section
    media_library_title = models.CharField(max_length=255, blank=True, default="Media Library")
    media_library_subtitle = models.CharField(max_length=255, blank=True, default="Watch past Vinelife Wilmslow talks and sermons.")
    media_library_main_videos = RichTextField(blank=True, help_text="HTML for main videos (iframe embed)")
    media_library_old_streams = RichTextField(blank=True, help_text="HTML for old live streams (iframe embed)")
    media_library_playlists = RichTextField(blank=True, help_text="HTML for playlists (iframe embed)")

    # Resources Section
    resources_title = models.CharField(max_length=255, blank=True, default="Resources")
    resources_subtitle = models.CharField(max_length=255, blank=True, default="Explore helpful resources in our community")
    resource_1_title = models.CharField(max_length=100, blank=True, default="Alpha")
    resource_1_url = models.URLField(blank=True, help_text="Alpha website link")
    resource_1_img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', help_text="Alpha logo")
    resource_2_title = models.CharField(max_length=100, blank=True, default="CAP")
    resource_2_url = models.URLField(blank=True, help_text="CAP website link")
    resource_2_img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', help_text="CAP logo")
    resource_3_title = models.CharField(max_length=100, blank=True, default="Hope Central")
    resource_3_url = models.URLField(blank=True, help_text="Hope Central website link")
    resource_3_img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', help_text="Hope Central logo")

    # Find Us Section
    find_us_title = models.CharField(max_length=255, blank=True, default="Find Us")
    map_embed = RichTextField(blank=True, help_text="Google Maps embed iframe HTML")
    parking_info = RichTextField(blank=True, help_text="Parking information")

    # Contact Section
    contact_title = models.CharField(max_length=255, blank=True, default="Contact us")
    contact_intro = models.CharField(max_length=255, blank=True, default="Get in touch with us!")
    contact_email = models.EmailField(blank=True, default="info@vinelifewilmslow.com")
    contact_phone = models.CharField(max_length=30, blank=True, default="07957 813360")
    contact_address = models.CharField(max_length=255, blank=True, default="")
    instagram_url = models.URLField(blank=True, help_text="Instagram link")

    # Wagtail admin panels for editing
    content_panels = Page.content_panels + [
        # Hero Section
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_image_1'),
            FieldPanel('hero_image_2'),
            FieldRowPanel([
                FieldPanel('hero_cta_1_label', classname='col6'),
                FieldPanel('hero_cta_1_link', classname='col6'),
            ]),
            FieldRowPanel([
                FieldPanel('hero_cta_2_label', classname='col6'),
                FieldPanel('hero_cta_2_link', classname='col6'),
            ]),
            FieldPanel('facebook_url'),
        ], heading='Hero Section'),
        
        # Mission Section
        MultiFieldPanel([
            FieldPanel('mission_title'),
            FieldPanel('mission_content'),
            FieldPanel('mission_readmore_label'),
            FieldPanel('mission_history_title'),
            FieldPanel('mission_history'),
        ], heading='Mission Section'),
        
        # Founders Section
        MultiFieldPanel([
            FieldPanel('founders_title'),
            FieldPanel('founders_image'),
            FieldPanel('founders_caption'),
            FieldPanel('founders_content'),
        ], heading='Founders Section'),
        
        # Thought for the Day Section
        MultiFieldPanel([
            FieldPanel('thought_title'),
        ], heading='Thought for the Day'),
        
        # Worship Meetings Section
        MultiFieldPanel([
            FieldPanel('worship_title'),
            FieldPanel('worship_subtitle'),
        ], heading='Worship Meetings'),
        
        # Special Events Section
        MultiFieldPanel([
            FieldPanel('special_events_title'),
            FieldPanel('special_events_subtitle'),
        ], heading='Special Events'),
        
        # Groups Section
        MultiFieldPanel([
            FieldPanel('groups_title'),
            FieldPanel('groups_subtitle'),
            FieldPanel('mens_group_title'),
            FieldPanel('mens_group_description'),
            FieldPanel('mens_group_meetings'),
            FieldPanel('mens_group_contact'),
            FieldPanel('womens_group_title'),
            FieldPanel('womens_group_description'),
            FieldPanel('womens_group_meetings'),
            FieldPanel('womens_group_contact'),
        ], heading='Groups Section'),
        
        # YouTube Section
        MultiFieldPanel([
            FieldPanel('youtube_channel_title'),
            FieldPanel('youtube_embed_url'),
            FieldPanel('youtube_url'),
        ], heading='YouTube Channel'),
        
        # Media Library Section
        MultiFieldPanel([
            FieldPanel('media_library_title'),
            FieldPanel('media_library_subtitle'),
            FieldPanel('media_library_main_videos'),
            FieldPanel('media_library_old_streams'),
            FieldPanel('media_library_playlists'),
        ], heading='Media Library'),
        
        # Resources Section
        MultiFieldPanel([
            FieldPanel('resources_title'),
            FieldPanel('resources_subtitle'),
            FieldPanel('resource_1_title'),
            FieldPanel('resource_1_url'),
            FieldPanel('resource_1_img'),
            FieldPanel('resource_2_title'),
            FieldPanel('resource_2_url'),
            FieldPanel('resource_2_img'),
            FieldPanel('resource_3_title'),
            FieldPanel('resource_3_url'),
            FieldPanel('resource_3_img'),
        ], heading='Resources'),
        
        # Find Us Section
        MultiFieldPanel([
            FieldPanel('find_us_title'),
            FieldPanel('map_embed'),
            FieldPanel('parking_info'),
        ], heading='Find Us'),
        
        # Contact Section
        MultiFieldPanel([
            FieldPanel('contact_title'),
            FieldPanel('contact_intro'),
            FieldPanel('contact_email'),
            FieldPanel('contact_phone'),
            FieldPanel('contact_address'),
            FieldPanel('instagram_url'),
        ], heading='Contact Section'),
    ]


class AlphaCoursePage(Page):
    """Alpha Course page with overview, what's covered, and sign-up info"""
    
    # Overview Section
    overview_title = models.CharField(max_length=255, blank=True, default="What is Alpha?")
    overview_content = RichTextField(blank=True, help_text="Description of Alpha course")
    overview_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Alpha course overview image"
    )
    
    # What's Covered Section
    covered_title = models.CharField(max_length=255, blank=True, default="What's Covered")
    covered_content = RichTextField(blank=True, help_text="Topics and sessions covered in the course")
    
    # Why Join Section
    why_join_title = models.CharField(max_length=255, blank=True, default="Why Join Alpha?")
    why_join_content = RichTextField(blank=True, help_text="Benefits and reasons to join")
    
    # YouTube Content
    youtube_title = models.CharField(max_length=255, blank=True, default="Alpha Videos")
    youtube_embed_1 = models.URLField(blank=True, help_text="YouTube embed URL 1")
    youtube_embed_2 = models.URLField(blank=True, help_text="YouTube embed URL 2")
    youtube_playlist_url = models.URLField(blank=True, help_text="Alpha YouTube playlist URL")
    
    # Local Information
    local_title = models.CharField(max_length=255, blank=True, default="Alpha at Vinelife Wilmslow")
    local_info = RichTextField(blank=True, help_text="Local session times and contact info")
    
    # Sign-Up Section
    signup_title = models.CharField(max_length=255, blank=True, default="Sign Up Today")
    signup_intro = models.CharField(max_length=255, blank=True, default="Ready to explore faith?")
    alpha_website_url = models.URLField(blank=True, default="https://alpha.org.uk/try-alpha")
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('overview_title'),
            FieldPanel('overview_image'),
            FieldPanel('overview_content'),
        ], heading='Overview'),
        
        MultiFieldPanel([
            FieldPanel('covered_title'),
            FieldPanel('covered_content'),
        ], heading='What\'s Covered'),
        
        MultiFieldPanel([
            FieldPanel('why_join_title'),
            FieldPanel('why_join_content'),
        ], heading='Why Join'),
        
        MultiFieldPanel([
            FieldPanel('youtube_title'),
            FieldPanel('youtube_embed_1'),
            FieldPanel('youtube_embed_2'),
            FieldPanel('youtube_playlist_url'),
        ], heading='YouTube Content'),
        
        MultiFieldPanel([
            FieldPanel('local_title'),
            FieldPanel('local_info'),
        ], heading='Local Information'),
        
        MultiFieldPanel([
            FieldPanel('signup_title'),
            FieldPanel('signup_intro'),
            FieldPanel('alpha_website_url'),
        ], heading='Sign Up'),
    ]


class CAPPage(Page):
    """Christians Against Poverty (CAP) page with services and support info"""
    
    # What is CAP Section
    about_title = models.CharField(max_length=255, blank=True, default="What is CAP?")
    about_content = RichTextField(blank=True, help_text="Introduction to CAP")
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="CAP logo or image"
    )
    
    # Services Section
    services_title = models.CharField(max_length=255, blank=True, default="Our Services")
    services_content = RichTextField(blank=True, help_text="Details about CAP services: debt help, money coaching, job clubs, life skills")
    
    # Impact Section
    impact_title = models.CharField(max_length=255, blank=True, default="Our Impact")
    impact_content = RichTextField(blank=True, help_text="Impact stories and statistics")
    people_helped = models.CharField(max_length=100, blank=True, default="35,000+", help_text="Number of people helped")
    
    # YouTube Content
    youtube_title = models.CharField(max_length=255, blank=True, default="CAP Videos")
    youtube_embed_1 = models.URLField(blank=True, help_text="YouTube embed URL 1")
    youtube_embed_2 = models.URLField(blank=True, help_text="YouTube embed URL 2")
    youtube_channel_url = models.URLField(blank=True, help_text="CAP YouTube channel URL")
    
    # Local Services
    local_title = models.CharField(max_length=255, blank=True, default="CAP at Vinelife Wilmslow")
    local_services = RichTextField(blank=True, help_text="Services available at Vinelife/Hope Central")
    
    # Get Help Section
    help_title = models.CharField(max_length=255, blank=True, default="Get Free Help")
    help_intro = RichTextField(blank=True, help_text="How to access CAP support")
    cap_website_url = models.URLField(blank=True, default="https://www.capuk.org/get-help/debt-help")
    local_contact = models.CharField(max_length=255, blank=True, help_text="Local contact info for referrals")
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('about_title'),
            FieldPanel('about_image'),
            FieldPanel('about_content'),
        ], heading='About CAP'),
        
        MultiFieldPanel([
            FieldPanel('services_title'),
            FieldPanel('services_content'),
        ], heading='Services'),
        
        MultiFieldPanel([
            FieldPanel('impact_title'),
            FieldPanel('people_helped'),
            FieldPanel('impact_content'),
        ], heading='Impact'),
        
        MultiFieldPanel([
            FieldPanel('youtube_title'),
            FieldPanel('youtube_embed_1'),
            FieldPanel('youtube_embed_2'),
            FieldPanel('youtube_channel_url'),
        ], heading='YouTube Content'),
        
        MultiFieldPanel([
            FieldPanel('local_title'),
            FieldPanel('local_services'),
        ], heading='Local Services'),
        
        MultiFieldPanel([
            FieldPanel('help_title'),
            FieldPanel('help_intro'),
            FieldPanel('local_contact'),
            FieldPanel('cap_website_url'),
        ], heading='Get Help'),
    ]


class HopeCentralPage(Page):
    """Hope Central page with services, impact, and involvement info"""
    
    # Mission Section
    mission_title = models.CharField(max_length=255, blank=True, default="About Hope Central")
    mission_content = RichTextField(blank=True, help_text="Hope Central mission and overview")
    mission_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Hope Central logo or image"
    )
    
    # Services Section
    services_title = models.CharField(max_length=255, blank=True, default="Services We Offer")
    services_content = RichTextField(blank=True, help_text="Food bank, pantry, job club, debt centre, money management, Alpha, Hope Centres")
    
    # Impact Section
    impact_title = models.CharField(max_length=255, blank=True, default="Our Impact")
    referrals_2024 = models.CharField(max_length=100, blank=True, default="3,400+", help_text="Number of referrals in 2024")
    meals_2024 = models.CharField(max_length=100, blank=True, default="65,500", help_text="Number of meals provided in 2024")
    impact_content = RichTextField(blank=True, help_text="Impact stats and stories")
    
    # Get Involved Section
    involved_title = models.CharField(max_length=255, blank=True, default="Get Involved")
    volunteer_content = RichTextField(blank=True, help_text="Volunteering opportunities")
    donate_url = models.URLField(blank=True, default="https://cafdonate.cafonline.org/17913")
    
    # Contact & Resources
    contact_title = models.CharField(max_length=255, blank=True, default="Contact Us")
    contact_info = RichTextField(blank=True, help_text="Contact information and hours")
    phone = models.CharField(max_length=20, blank=True, default="01625 724 133")
    email = models.EmailField(blank=True, default="info@hopecentral.org.uk")
    website_url = models.URLField(blank=True, default="https://www.hopecentral.org.uk")
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('mission_title'),
            FieldPanel('mission_image'),
            FieldPanel('mission_content'),
        ], heading='Mission'),
        
        MultiFieldPanel([
            FieldPanel('services_title'),
            FieldPanel('services_content'),
        ], heading='Services'),
        
        MultiFieldPanel([
            FieldPanel('impact_title'),
            FieldPanel('referrals_2024'),
            FieldPanel('meals_2024'),
            FieldPanel('impact_content'),
        ], heading='Impact'),
        
        MultiFieldPanel([
            FieldPanel('involved_title'),
            FieldPanel('volunteer_content'),
            FieldPanel('donate_url'),
        ], heading='Get Involved'),
        
        MultiFieldPanel([
            FieldPanel('contact_title'),
            FieldPanel('phone'),
            FieldPanel('email'),
            FieldPanel('contact_info'),
            FieldPanel('website_url'),
        ], heading='Contact Information'),
    ]


