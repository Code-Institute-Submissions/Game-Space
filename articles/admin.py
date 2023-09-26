from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin


# Article admin display.
@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    # full list display of entities
    list_display = ('title', 'slug', 'author', 'created_on',
                    'status', 'number_of_likes')
    # Filters
    list_filter = ('status', 'created_on', 'author')
    # Serach fields
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    # Summer note custom text field
    summernote_fields = ('content',)

    def number_of_likes(self, obj):
        # likes column
        return obj.likes.count()
    number_of_likes.short_description = 'Likes'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # full list display of entities
    list_display = ('name', 'article', 'user', 'created_on', 'approved')
    # Filters
    list_filter = ('approved', 'created_on', 'user')
    # Serach fields
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
