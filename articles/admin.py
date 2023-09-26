from django.contrib import admin
from .models import Article, Comment
# If you are using django_summernote for Article content
from django_summernote.admin import SummernoteModelAdmin


class ArticleAdmin(SummernoteModelAdmin):
    # Valid attributes of Article
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')  # Valid attributes of Article
    list_filter = ('status', 'created_on')  # Valid attributes of Article
    prepopulated_fields = {'slug': ('title',)}
    # Enable Summernote for the content field (if using django_summernote)
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'article', 'created_on',
                    'approved')  # Valid attributes of Comment
    list_filter = ('approved', 'created_on')  # Valid attributes of Comment
    search_fields = ('name', 'content')  # Valid attributes of Comment
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
