from django.contrib import admin
from .models import Blog,BlogCategory,Comments,BlogTag
from django.utils.html import format_html
from django.db.models import F
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'categories', 'is_active', 'cover_image')
    list_filter = ['categories', 'is_active']

@admin.register(BlogTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ['translations__title']

@admin.register(BlogCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ['translations__title']

    
@admin.register(Comments)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('comment',)
    search_fields = ['translations__comment']


 

    def view_cover_image(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.cover_image.url))
        return None
    view_cover_image.short_description = 'Cover Image'


