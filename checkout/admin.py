from django.contrib import admin
from checkout.models import ShoppingCart, CartItem
from modeltranslation.admin import TranslationAdmin
# Register your models here.

admin.site.register(ShoppingCart)
admin.site.register(CartItem)

# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('cart', 'product_version', 'quantity')
#     search_fields = ['cart', 'product_version']
