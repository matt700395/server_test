from django.contrib import admin

# Register your models here.
from articleapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
