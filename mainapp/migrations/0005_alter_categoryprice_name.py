# Generated by Django 4.0.1 on 2022-01-10 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_categoryprice_remove_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryprice',
            name='name',
            field=models.IntegerField(default=0, null=True, verbose_name='product_price'),
        ),
    ]