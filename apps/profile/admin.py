from django.contrib import admin

from apps.profile.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'tc']
    search_fields = ('user', 'tc',)
    autocomplete_fields = ["user"]
