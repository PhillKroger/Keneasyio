# Generated by Django 4.0.1 on 2022-01-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_categoryclothes_img_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='img'),
        ),
    ]
