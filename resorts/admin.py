from django.contrib import admin
from .models import Resort
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Resort)
class ResortAdmin(SummernoteModelAdmin):
    search_fields = ('resort', 'name', 'country', 'user_name')
    list_display = ('resort', 'country')
    list_filter = ('status',)
    summernote_fields = ('description')
