from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html
from django.db.models import F
from .models import Brand, ProductTag, ProductCategory, Product, Color, ProductVersion, ProductVersionImage, ProductVersionReview, Wishlist

admin.site.register(Wishlist)
def mark_products_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)
mark_products_inactive.short_description = "Mark selected products as inactive"

def increase_quantity_by_10(modeladmin, request, queryset):
    queryset.update(quantity=F('quantity') + 10)
increase_quantity_by_10.short_description = "Increase quantity of selected products by 10"


@admin.register(Brand)
class BrandAdmin(TranslationAdmin):
    list_display = ('title', 'is_active')
    search_fields = ['translations__title']

@admin.register(ProductTag)
class ProductTagAdmin(TranslationAdmin):
    list_display = ('title', 'is_active')
    search_fields = ['translations__title']

@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('title', 'is_active')
    search_fields = ['translations__title']

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'brand','slug', 'category', 'is_active', 'view_cover_image')
    list_filter = ['brand', 'category', 'is_active']
    search_fields = ['translations__title', 'translations__description']

    actions = [mark_products_inactive]

    def view_cover_image(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.cover_image.url))
        return None
    view_cover_image.short_description = 'Cover Image'

@admin.register(Color)
class ColorAdmin(TranslationAdmin):
    list_display = ('title', 'hex_code', 'is_active')
    search_fields = ['translations__title']

@admin.register(ProductVersion)
class ProductVersionAdmin(TranslationAdmin):
    list_display = ('title', 'product', 'price','slug', 'quantity', 'is_active')
    list_filter = ['product__brand', 'color', 'tags']
    search_fields = ['translations__title', 'translations__description']

    actions = [increase_quantity_by_10]

@admin.register(ProductVersionImage)
class ProductVersionImageAdmin(admin.ModelAdmin):
    list_display = ('product_version', 'image', 'is_active')
    search_fields = ['product_version']

@admin.register(ProductVersionReview)
class ProductVersionReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'product_version', 'comment')
    search_fields = ['full_name', 'comment', ]




