# Generated by Django 4.0.1 on 2022-02-10 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
                ('description', models.TextField()),
                ('prise', models.DecimalField(decimal_places=0, max_digits=7)),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('avtor', models.CharField(max_length=130)),
            ],
            options={
                'verbose_name': 'Ware',
                'verbose_name_plural': 'Wares',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('item_total', models.DecimalField(decimal_places=0, max_digits=9)),
                ('ware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ware')),
            ],
            options={
                'verbose_name': 'CartItem',
                'verbose_name_plural': 'CartItems',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_total', models.DecimalField(decimal_places=0, max_digits=9)),
                ('items', models.ManyToManyField(blank=True, to='mainapp.CartItem')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
    ]