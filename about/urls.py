from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
    # other URL patterns for the about app
]