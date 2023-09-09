from django.contrib import admin
from .models import Article, Tag, Category, Comment, Newsletter, Season


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date']
    list_filter = ['created_date']
    exclude = ['like', 'views']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'message']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
