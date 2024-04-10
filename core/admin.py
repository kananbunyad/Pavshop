from django.contrib import admin
from .models import Contact,Newsletter
# Register your models here.


class ContactAdmin (admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'subject', 'message')

    list_filter = ['full_name']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
