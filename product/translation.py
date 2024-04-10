# models/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import Brand, ProductTag, ProductCategory, Product, Color, ProductVersion, ProductVersionImage, ProductVersionReview, Wishlist

@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ProductTag)
class ProductTagTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Color)
class ColorTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ProductVersion)
class ProductVersionTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)




