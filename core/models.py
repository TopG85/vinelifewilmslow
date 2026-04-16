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


