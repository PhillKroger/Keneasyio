# Generated by Django 4.0.1 on 2022-02-10 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_ware_cartitem_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='ware',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Ware',
        ),
    ]
