# Generated by Django 4.2.6 on 2024-01-30 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_color_title_az_color_title_en_color_title_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='producttag',
            name='slug',
        ),
    ]
