#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vinelife_cms.settings')
django.setup()

from wagtail.models import Page
from core.models import (
    HomePage, MissionPage, LeadershipPage, WorshipPage,
    GroupsPage, ResourcesPage, ContactPage, YouTubePage, NotificationPage
)

# Get the root page (site root)
root = Page.get_first_root_node()

# Create Home Page
if not HomePage.objects.exists():
    home = HomePage(
        title="Home",
        slug="home",
        hero_title="Welcome to Vinelife Wilmslow",
        hero_subtitle="A community church in the heart of Wilmslow, Cheshire",
        hero_cta_text="Learn More",
        hero_cta_url="/mission/",
        facebook_url="https://www.facebook.com/vinelifewilmslow"
    )
    root.add_child(instance=home)
    home.save_revision().publish()
    print("✅ Home Page created")

# Create Mission Page
if not MissionPage.objects.exists():
    mission = MissionPage(
        title="Our Mission",
        slug="mission",
        main_content="<p>Vinelife Wilmslow is a vibrant community church dedicated to spreading the Gospel and serving our local community.</p><p>We believe in creating a welcoming space where everyone can encounter God's love and grow in their faith.</p>"
    )
    root.add_child(instance=mission)
    mission.save_revision().publish()
    print("✅ Mission Page created")

# Create Leadership Page
if not LeadershipPage.objects.exists():
    leadership = LeadershipPage(
        title="Leadership",
        slug="leadership",
        intro="<p>Meet our church leaders and team members.</p>"
    )
    root.add_child(instance=leadership)
    leadership.save_revision().publish()
    print("✅ Leadership Page created")

# Create Worship Page
if not WorshipPage.objects.exists():
    worship = WorshipPage(
        title="Worship & Services",
        slug="worship",
        intro="<p>Join us for Sunday worship services and special events.</p>"
    )
    root.add_child(instance=worship)
    worship.save_revision().publish()
    print("✅ Worship Page created")

# Create Groups Page
if not GroupsPage.objects.exists():
    groups = GroupsPage(
        title="Groups",
        slug="groups",
        intro="<p>Connect with our church groups and ministries.</p>"
    )
    root.add_child(instance=groups)
    groups.save_revision().publish()
    print("✅ Groups Page created")

# Create Resources Page
if not ResourcesPage.objects.exists():
    resources = ResourcesPage(
        title="Local Resources",
        slug="resources",
        intro="<p>Community resources and support services available in Wilmslow.</p>"
    )
    root.add_child(instance=resources)
    resources.save_revision().publish()
    print("✅ Resources Page created")

# Create Contact Page
if not ContactPage.objects.exists():
    contact = ContactPage(
        title="Contact Us",
        slug="contact",
        intro="<p>Get in touch with Vinelife Wilmslow.</p>",
        email="info@vinelifewilmslow.com",
        phone="+44 (0) 1625 525000",
        address="<p>The Open Arms Youth Project<br>Howty Close<br>Wilmslow, Cheshire SK9 2SH</p>"
    )
    root.add_child(instance=contact)
    contact.save_revision().publish()
    print("✅ Contact Page created")

# Create YouTube Page
if not YouTubePage.objects.exists():
    youtube = YouTubePage(
        title="YouTube",
        slug="youtube",
        channel_url="https://www.youtube.com/channel/UC0G20x3mVQwmqGUAig_MAcA",
        description="<p>Watch our sermons, worship services, and special events on our YouTube channel.</p>"
    )
    root.add_child(instance=youtube)
    youtube.save_revision().publish()
    print("✅ YouTube Page created")

# Create Notification Page
if not NotificationPage.objects.exists():
    notification = NotificationPage(
        title="Thought for the Day",
        slug="thought",
        current_message="<p>Check back for daily inspirational messages from our church community.</p>",
        author="Vinelife Team"
    )
    root.add_child(instance=notification)
    notification.save_revision().publish()
    print("✅ Thought for the Day Page created")

print("\n🎉 All pages created and published!")
print("📝 Visit http://127.0.0.1:8001/admin/ to edit them.")
print("🌐 View them live at http://127.0.0.1:8001/")
