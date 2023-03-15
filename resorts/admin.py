from django.contrib import admin
from .models import Resort, Contact, Rating, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Resort)
class ResortAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('resort',)}
    search_fields = ['resort', 'name', 'country', 'user_name']
    list_display = ('resort', 'country', 'status', 'average_rating')
    list_filter = ('status',)
    summernote_fields = ('description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('resort', 'user')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
