# Generated by Django 4.2.6 on 2024-02-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_productversion_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='productversionreview',
            name='raiting',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]