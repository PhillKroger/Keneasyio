# Generated by Django 4.0.1 on 2022-02-10 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_alter_post_text_alter_post_title_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='set_product',
        ),
        migrations.AddField(
            model_name='set',
            name='set_product_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.categoryprice', verbose_name='CategoryPrice'),
        ),
    ]