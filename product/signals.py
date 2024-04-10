from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify
from product.models import Product,ProductVersion


@receiver(post_save, sender=Product)
def ProductSave(sender, created, **kwargs):
    if created:
        instance = kwargs["instance"]
        instance.slug = slugify(instance.title, replacements=[['n', 'm']])
        instance.slug = instance.slug + '-' + str(datetime.now().timestamp()).replace('.', '')[:10]
        instance.save()
    

# @receiver(post_save, sender=ProductVersion)
# def ProductVersionSave(sender, created, **kwargs):
#     if created:
#         instance = kwargs["instance"]
#         instance.slug = slugify(instance.title, replacements=[['n', 'm']])
#         instance.slug = instance.slug + '-' + str(datetime.now().timestamp()).replace('.', '')[:10]
#         instance.save()