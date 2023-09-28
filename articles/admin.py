from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    # full list display of entities
    list_display = ('title', 'slug', 'status', 'created_on')
    # Filters
    list_filter = ('status', 'created_on')
    # Serach fields
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # Summer note custom text field
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # full list display of entities
    list_display = ('name', 'article', 'user', 'created_on', 'approved')
    # Filters
    list_filter = ('approved', 'created_on')
    # Serach fields
    search_fields = ('name', 'email', 'body',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
