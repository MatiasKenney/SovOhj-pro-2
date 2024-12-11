from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry

@login_required
def topics(request):
    """Show all topics."""
    # Your function logic here

