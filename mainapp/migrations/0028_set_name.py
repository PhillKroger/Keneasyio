# Generated by Django 4.0.1 on 2022-02-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_remove_set_set_product_1_set_pr'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
    ]