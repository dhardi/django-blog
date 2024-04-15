from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.
def about(request):
    # Retrieve the About object, assuming there's only one instance
    about_info = About.objects.first()
    