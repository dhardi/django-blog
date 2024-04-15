from django.contrib import admin
from .models import About

# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_on')