# Generated by Django 4.0.1 on 2022-01-29 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
    ]
