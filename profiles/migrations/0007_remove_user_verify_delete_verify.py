# Generated by Django 4.0.2 on 2022-03-08 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_verify_remove_user_verified_user_verify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='verify',
        ),
        migrations.DeleteModel(
            name='Verify',
        ),
    ]