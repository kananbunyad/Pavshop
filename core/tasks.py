import time
from celery import shared_task
from shop import settings
from django.template.loader import render_to_string
from product.models import ProductVersion
from core.models import Newsletter
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


@shared_task
def export():
    time.sleep(5)


@shared_task
def send_email():
    subs = list(Newsletter.objects.values_list('email', flat=True))
    product_version = ProductVersion.objects.all()
    print(product_version)
    subject = "New Products"
    text_content = "This is an important message."
    for sub in subs:
        message = render_to_string('email-subscriber.html', {
                    "product_version": product_version,
                    "name": sub,
                })
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [sub])
        msg.attach_alternative(message, "text/html")
        msg.send()


def send_popular_products_email():

    inactive_users = User.objects.filter(last_login__lt=timezone.now() - timedelta(days=30))
    
    # Son bir ay ərzində ən çox review yazılmış beş məhsulu tapmaq
    popular_products = ProductVersion.objects.all()
    
    for user in inactive_users:
        message = render_to_string('email_template.html', {'products': popular_products, 'user': user})
        send_email(
            'Biz Sizi Çox Gözlədik! Bu Ayın Ən Populyar Məhsullarına Göz Atın',
            message,)
        msg = EmailMultiAlternatives(inactive_users, popular_products, settings.EMAIL_HOST_USER, [user])
        msg.attach_alternative(message, "text/html")
        msg.send()