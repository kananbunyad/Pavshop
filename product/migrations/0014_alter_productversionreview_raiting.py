# Generated by Django 4.2.6 on 2024-02-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0013_remove_wishlist_product_wishlist_product_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productversionreview",
            name="raiting",
            field=models.IntegerField(null=True),
        ),
    ]
