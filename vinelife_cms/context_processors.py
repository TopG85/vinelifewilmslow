"""
Context processors for passing settings to templates.
"""

import os


def api_config(request):
    """
    Add API configuration to template context.
    These values are loaded from environment variables.
    """
    return {
        'google_calendar_id': os.getenv('GOOGLE_CALENDAR_ID', ''),
        'google_calendar_api_key': os.getenv('GOOGLE_CALENDAR_API_KEY', ''),
        'formspree_endpoint': os.getenv('FORMSPREE_ENDPOINT', ''),
        'bible_api_enabled': os.getenv('BIBLE_API_ENABLED', 'true').lower() == 'true',
        'bible_api_translation': os.getenv('BIBLE_API_TRANSLATION', 'kjv'),
    }
