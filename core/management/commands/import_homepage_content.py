import os
from django.core.management.base import BaseCommand
from django.db import transaction
from wagtail.models import Page, Site
from core.models import HomePage
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Import homepage content from index.html into the HomePage model.'

    def handle(self, *args, **options):
        # Path to index.html (adjust if needed)
        index_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'index.html')
        if not os.path.exists(index_path):
            self.stderr.write(self.style.ERROR(f'index.html not found at {index_path}'))
            return

        with open(index_path, encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # --- HERO SECTION ---
        hero_title = soup.select_one('section#hero h1')
        hero_title = hero_title.get_text(strip=True) if hero_title else ''
        hero_img_1 = soup.select_one('#hero-img-1')
        hero_img_1_src = hero_img_1['src'] if hero_img_1 and hero_img_1.has_attr('src') else ''
        hero_img_2 = soup.select_one('#hero-img-2')
        hero_img_2_src = hero_img_2['src'] if hero_img_2 and hero_img_2.has_attr('src') else ''
        facebook_link = soup.select_one('.social-links a[href*="facebook.com"]')
        facebook_url = facebook_link['href'] if facebook_link and facebook_link.has_attr('href') else ''

        # --- MISSION SECTION ---
        mission_section = soup.select_one('#about-content')
        mission_content = ''
        mission_history = ''
        if mission_section:
            mission_paras = mission_section.find_all('p', recursive=False)
            if mission_paras:
                mission_content = mission_paras[0].get_text(strip=True)
            # History is in the hidden div
            history_div = mission_section.select_one('#about-full-text')
            if history_div:
                mission_history = '\n'.join([p.get_text(strip=True) for p in history_div.find_all('p')])

        # --- FOUNDERS SECTION ---
        founders_section = soup.select_one('#founders-content')
        founders_content = ''
        founders_image_src = ''
        if founders_section:
            founders_paras = founders_section.find_all('p')
            founders_content = '\n'.join([p.get_text(strip=True) for p in founders_paras])
            founders_img = founders_section.select_one('img')
            if founders_img and founders_img.has_attr('src'):
                founders_image_src = founders_img['src']

        # --- THOUGHT FOR THE DAY ---
        thought_title = 'Thought for the Day'

        # --- WORSHIP SECTION ---
        worship_title = ''
        worship_subtitle = ''
        worship_title_el = soup.select_one('#worship-title')
        if worship_title_el:
            worship_title = worship_title_el.get_text(strip=True)
        worship_subtitle_el = soup.select_one('#events .text-lg')
        if worship_subtitle_el:
            worship_subtitle = worship_subtitle_el.get_text(strip=True)

        # --- GROUPS SECTION ---
        groups_title = ''
        groups_subtitle = ''
        mens_group_description = ''
        mens_group_contact = ''
        womens_group_description = ''
        womens_group_contact = ''
        groups_section = soup.select_one('#groups')
        if groups_section:
            groups_title_el = groups_section.select_one('h2')
            if groups_title_el:
                groups_title = groups_title_el.get_text(strip=True)
            groups_subtitle_el = groups_section.select_one('#groups-subtitle')
            if groups_subtitle_el:
                groups_subtitle = groups_subtitle_el.get_text(strip=True)
            mens_box = groups_section.find('h3', string=lambda t: t and "Men's Group" in t)
            if mens_box:
                mens_group_description = mens_box.find_next('p').get_text(strip=True)
                mens_group_contact_el = mens_box.find_next('a', href=lambda h: h and '07957' in h)
                if mens_group_contact_el:
                    mens_group_contact = mens_group_contact_el.get_text(strip=True)
            womens_box = groups_section.find('h3', string=lambda t: t and "Women's Group" in t)
            if womens_box:
                womens_group_description = womens_box.find_next('p').get_text(strip=True)
                womens_group_contact_el = womens_box.find_next('a', href=lambda h: h and '07942' in h)
                if womens_group_contact_el:
                    womens_group_contact = womens_group_contact_el.get_text(strip=True)

        # --- SPECIAL EVENTS ---
        special_events_title = ''
        special_events_subtitle = ''
        special_events_section = soup.select_one('#special-events-center-wrapper')
        if special_events_section:
            se_title_el = special_events_section.select_one('h2')
            if se_title_el:
                special_events_title = se_title_el.get_text(strip=True)
            se_subtitle_el = special_events_section.select_one('p')
            if se_subtitle_el:
                special_events_subtitle = se_subtitle_el.get_text(strip=True)

        # --- YOUTUBE ---
        youtube_channel_title = ''
        youtube_embed_url = ''
        youtube_section = soup.select_one('#youtube')
        if youtube_section:
            yt_title_el = youtube_section.select_one('h2')
            if yt_title_el:
                youtube_channel_title = yt_title_el.get_text(strip=True)
            yt_iframe = youtube_section.select_one('iframe')
            if yt_iframe and yt_iframe.has_attr('src'):
                youtube_embed_url = yt_iframe['src']

        # --- MEDIA LIBRARY ---
        media_library_title = ''
        media_library_subtitle = ''
        media_library_section = soup.select_one('#media-library')
        if media_library_section:
            ml_title_el = media_library_section.select_one('h2')
            if ml_title_el:
                media_library_title = ml_title_el.get_text(strip=True)
            ml_subtitle_el = media_library_section.select_one('p')
            if ml_subtitle_el:
                media_library_subtitle = ml_subtitle_el.get_text(strip=True)

        # --- RESOURCES ---
        resources_title = ''
        resources_subtitle = ''
        resources_section = soup.select_one('#local-resources')
        if resources_section:
            res_title_el = resources_section.select_one('h2')
            if res_title_el:
                resources_title = res_title_el.get_text(strip=True)
            res_subtitle_el = resources_section.select_one('p')
            if res_subtitle_el:
                resources_subtitle = res_subtitle_el.get_text(strip=True)

        # --- FIND US ---
        find_us_title = ''
        parking_info = ''
        map_embed = ''
        find_us_section = soup.select_one('#find-us')
        if find_us_section:
            find_title_el = find_us_section.select_one('h2')
            if find_title_el:
                find_us_title = find_title_el.get_text(strip=True)
            parking_el = find_us_section.find('h2', string=lambda t: t and 'Parking' in t)
            if parking_el:
                parking_info_el = parking_el.find_next('p')
                if parking_info_el:
                    parking_info = parking_info_el.get_text(strip=True)
            map_iframe = find_us_section.select_one('iframe')
            if map_iframe and map_iframe.has_attr('src'):
                map_embed = map_iframe['src']

        # --- CONTACT ---
        contact_title = ''
        contact_intro = ''
        contact_email = ''
        contact_phone = ''
        contact_address = ''
        instagram_url = ''
        youtube_url = ''
        contact_section = soup.select_one('footer#contact')
        if contact_section:
            contact_title_el = contact_section.select_one('h2')
            if contact_title_el:
                contact_title = contact_title_el.get_text(strip=True)
            contact_intro = "Have a question? We'd love to hear from you!"
            email_link = contact_section.select_one('a[href^="mailto:"]')
            if email_link:
                contact_email = email_link.get_text(strip=True)
            phone_link = contact_section.select_one('a[href^="tel:"]')
            if phone_link:
                contact_phone = phone_link.get_text(strip=True)
            fb_link = contact_section.select_one('a[href*="facebook.com"]')
            if fb_link and fb_link.has_attr('href'):
                facebook_url = fb_link['href']

        with transaction.atomic():
            # Find or create HomePage as root
            root = Page.get_first_root_node()
            homepage = HomePage.objects.live().first()
            if not homepage:
                homepage = HomePage(title='Home', slug='home')
                root.add_child(instance=homepage)
                homepage.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('Created new HomePage.'))
            else:
                self.stdout.write(self.style.SUCCESS('Updating existing HomePage.'))

            # Images must be set manually in Wagtail admin
            homepage.hero_image_1 = None
            homepage.hero_image_2 = None
            homepage.facebook_url = facebook_url
            homepage.mission_content = mission_content
            homepage.mission_history = mission_history
            homepage.founders_content = founders_content
            homepage.thought_title = thought_title
            homepage.worship_title = worship_title
            homepage.worship_subtitle = worship_subtitle
            homepage.groups_title = groups_title
            homepage.groups_subtitle = groups_subtitle
            homepage.mens_group_description = mens_group_description
            homepage.mens_group_contact = mens_group_contact
            homepage.womens_group_description = womens_group_description
            homepage.womens_group_contact = womens_group_contact
            homepage.special_events_title = special_events_title
            homepage.special_events_subtitle = special_events_subtitle
            homepage.youtube_channel_title = youtube_channel_title
            homepage.youtube_embed_url = youtube_embed_url
            homepage.media_library_title = media_library_title
            homepage.media_library_subtitle = media_library_subtitle
            homepage.resources_title = resources_title
            homepage.resources_subtitle = resources_subtitle
            homepage.find_us_title = find_us_title
            homepage.parking_info = parking_info
            homepage.map_embed = map_embed
            homepage.contact_title = contact_title
            homepage.contact_intro = contact_intro
            homepage.contact_email = contact_email
            homepage.contact_phone = contact_phone
            homepage.contact_address = contact_address
            homepage.instagram_url = instagram_url
            homepage.youtube_url = youtube_url
            homepage.save_revision().publish()
            self.stdout.write(self.style.SUCCESS('HomePage content imported.'))

        # Set as root page for Site if not already
        site = Site.objects.first()
        if site and site.root_page != homepage:
            site.root_page = homepage
            site.save()
            self.stdout.write(self.style.SUCCESS('Set HomePage as root page for Site.'))

        self.stdout.write(self.style.SUCCESS('Import complete.'))
