from django.shortcuts import render
from .models import (
    HeroSection,
    MissionSection,
    FoundersSection,
    GroupSection,
    FindUsSection,
)


def home(request):
    """Render the homepage with all CMS sections."""
    context = {
        "hero": HeroSection.objects.first(),
        "mission": MissionSection.objects.first(),
        "founders_section": FoundersSection.objects.first(),
        "founders": None,
        "groups": GroupSection.objects.all(),
        "find_us": FindUsSection.objects.first(),
    }

    # Get all founders if founders section exists
    if context["founders_section"]:
        context["founders"] = context["founders_section"].founder_set.all()

    return render(request, "core/home.html", context)
