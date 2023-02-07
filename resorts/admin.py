from django.contrib import admin
from .models import Resort
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Resort)
class ResortAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
