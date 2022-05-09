# Generated by Django 4.0.1 on 2022-01-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_remove_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryimage',
            name='name',
        ),
        migrations.AlterField(
            model_name='categoryimage',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/category_image', verbose_name='img'),
        ),
    ]