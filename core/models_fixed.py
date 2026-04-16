from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey


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
    facebook_url = models.URLField(blank=True, default='https://www.facebook.com/VinelifeChurchWilmslow')
    
    # Mission Section
    mission_content = RichTextField(blank=True)
    mission_history = RichTextField(blank=True)
    
    # Founders Section
    founders_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Founders photo"
    )
    founders_content = RichTextField(blank=True)
    
    # Thought for Day
    thought_title = models.CharField(max_length=255, blank=True, default="Thought for the Day")
    
    # Worship/Events
    worship_title = models.CharField(max_length=255, blank=True, default="Sunday Worship Meetings")
    worship_subtitle = models.CharField(max_length=255, blank=True, default="Stay connected with what's happening at Vinelife Wilmslow")
    
    # Groups
    groups_title = models.CharField(max_length=255, blank=True, default="Groups at Vinelife Church")
    groups_subtitle = models.CharField(max_length=255, blank=True, default="We have groups for men & women.")
    mens_group_description = RichTextField(blank=True)
    mens_group_contact = models.CharField(max_length=20, blank=True, default="07957 813360")
    womens_group_description = RichTextField(blank=True)
    womens_group_contact = models.CharField(max_length=20, blank=True, default="07942 876042")
    
    # Special events
    special_events_title = models.CharField(max_length=255, blank=True, default="Special Events")
    special_events_subtitle = models.CharField(max_length=255, blank=True)
    
    # YouTube
    youtube_channel_title = models.CharField(max_length=255, blank=True, default="YouTube Channel")
    youtube_embed_url = models.URLField(blank=True, default='https://www.youtube.com/embed/7ZSEQlR2YZs')
    
    # Media Library
    media_library_title = models.CharField(max_length=255, blank=True, default="Media Library")
    media_library_subtitle = models.CharField(max_length=255, blank=True, default="Watch past Vinelife Wilmslow talks and sermons.")
    
    # Resources
    resources_title = models.CharField(max_length=255, blank=True, default="Resources")
    resources_subtitle = models.CharField(max_length=255, blank=True, default="Explore helpful resources in our community")
    
    # Find Us
    find_us_title = models.CharField(max_length=255, blank=True, default="Find Us")
    parking_info = RichTextField(blank=True)
    map_embed = models.TextField(blank=True, help_text="Google Maps embed iframe code")
    
    # Contact
    contact_title = models.CharField(max_length=255, blank=True, default="Contact us")
    contact_intro = models.CharField(max_length=500, blank=True, default="Have a question? We'd love to hear from you!")
    contact_email = models.EmailField(blank=True, default='info@vinelifewilmslow.com')
    contact_phone = models.CharField(max_length=20, blank=True, default='07957 813 360')
    contact_address = models.CharField(max_length=500, blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_image_1'),
            FieldPanel('hero_image_2'),
            FieldPanel('facebook_url'),
        ], heading="Hero Section"),
        
        MultiFieldPanel([
            FieldPanel('mission_content'),
            FieldPanel('mission_history'),
        ], heading="Mission Section"),
        
        MultiFieldPanel([
            FieldPanel('founders_image'),
            FieldPanel('founders_content'),
        ], heading="Founders Section"),
        
        MultiFieldPanel([
            FieldPanel('thought_title'),
        ], heading="Thought for the Day Section"),
        
        MultiFieldPanel([
            FieldPanel('worship_title'),
            FieldPanel('worship_subtitle'),
        ], heading="Worship Section"),
        
        MultiFieldPanel([
            FieldPanel('groups_title'),
            FieldPanel('groups_subtitle'),
            FieldPanel('mens_group_description'),
            FieldPanel('mens_group_contact'),
            FieldPanel('womens_group_description'),
            FieldPanel('womens_group_contact'),
        ], heading="Groups Section"),
        
        MultiFieldPanel([
            FieldPanel('special_events_title'),
            FieldPanel('special_events_subtitle'),
        ], heading="Special Events Section"),
        
        MultiFieldPanel([
            FieldPanel('youtube_channel_title'),
            FieldPanel('youtube_embed_url'),
        ], heading="YouTube Section"),
        
        MultiFieldPanel([
            FieldPanel('media_library_title'),
            FieldPanel('media_library_subtitle'),
        ], heading="Media Library Section"),
        
        MultiFieldPanel([
            FieldPanel('resources_title'),
            FieldPanel('resources_subtitle'),
        ], heading="Resources Section"),
        
        MultiFieldPanel([
            FieldPanel('find_us_title'),
            FieldPanel('map_embed'),
            FieldPanel('parking_info'),
        ], heading="Find Us Section"),
        
        MultiFieldPanel([
            FieldPanel('contact_title'),
            FieldPanel('contact_intro'),
            FieldPanel('contact_email'),
            FieldPanel('contact_phone'),
            FieldPanel('contact_address'),
            FieldPanel('facebook_url'),
            FieldPanel('instagram_url'),
            FieldPanel('youtube_url'),
        ], heading="Contact Section"),
    ]

    def __str__(self):
        return "Home Page"

    def get_template(self, request, *args, **kwargs):
        return 'core/home_page.html'

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class MissionPage(Page):
    """Mission/About page"""
    main_content = RichTextField()
    extended_content = RichTextField(blank=True, help_text="Extended history or additional details")
    
    content_panels = Page.content_panels + [
        FieldPanel('main_content'),
        FieldPanel('extended_content'),
    ]

    def __str__(self):
        return "Mission Page"

    def get_template(self, request, *args, **kwargs):
        return 'core/mission_page.html'

    class Meta:
        verbose_name = "Mission Page"


class LeadershipPage(Page):
    """Leadership/Founders page with team members"""
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('team_members', label='Team Members'),
    ]

    def __str__(self):
        return "Leadership Page"

    def get_template(self, request, *args, **kwargs):
        return 'core/leadership_page.html'

    class Meta:
        verbose_name = "Leadership Page"


class TeamMember(Orderable):
    """Team member for Leadership page"""
    page = ParentalKey(LeadershipPage, on_delete=models.CASCADE, related_name='team_members')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True)
    bio = RichTextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('role'),
        FieldPanel('bio'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name


class WorshipPage(Page):
    """Worship/Events page"""
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('service_times', label='Service Times'),
    ]

    def __str__(self):
        return "Worship Page"

    def get_template(self, request, *args, **kwargs):
        return 'core/worship_page.html'

    class Meta:
        verbose_name = "Worship Page"


class ServiceTime(Orderable):
    """Service time for Worship page"""
    page = ParentalKey(WorshipPage, on_delete=models.CASCADE, related_name='service_times')
    title = models.CharField(max_length=255)
    description = RichTextField()
    day_and_time = models.CharField(max_length=255, help_text="e.g., 'Sunday 10am'")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('day_and_time'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.title


class GroupsPage(Page):
    """Groups/Small Groups page"""
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('groups', label='Groups'),
    ]

    def __str__(self):
        return "Groups Page"

    def get_template(self, request, *args, **kwargs):
        return 'core/groups_page.html'

    class Meta:
        verbose_name = "Groups Page"


class Group(Orderable):
    """Group listing"""
    page = ParentalKey(GroupsPage, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=255)
    description = RichTextField()
    meeting_time = models.CharField(max_length=255, help_text="e.g., 'Thursdays 7-8:30pm'")
    contact_person = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('meeting_time'),
        FieldPanel('contact_person'),
        FieldPanel('contact_email'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name


class ResourcesPage(Page):
    """Community Resources/Links page"""
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('resources', label='Resources'),
    ]

    def __str__(self):
        return "Resources Page"

    def get_template(self, request, *args, **kwargs):
        return 'core/resources_page.html'

    class Meta:
        verbose_name = "Resources Page"


class Resource(Orderable):
    """Community resource"""
    page = ParentalKey(ResourcesPage, on_delete=models.CASCADE, related_name='resources')
    name = models.CharField(max_length=255)
    description = RichTextField()
    url = models.URLField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('url'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name


class ContactPage(Page):
    """Contact page"""
    intro = RichTextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = RichTextField(blank=True)
    office_hours = RichTextField(blank=True)
    map_embed = models.TextField(blank=True, help_text="Embed code from Google Maps (iframe)")
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('phone'),
        ], heading="Contact Information"),
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('office_hours'),
        ], heading="Location & Hours"),
        FieldPanel('map_embed'),
    ]

    def __str__(self):
        return "Contact Page"

    def get_template(self, request, *args, **kwargs):
        return 'core/contact_page.html'

    class Meta:
        verbose_name = "Contact Page"
