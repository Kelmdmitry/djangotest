from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'pub_date']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

