# Generated by Django 2.0.7 on 2020-04-25 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='category',
            new_name='title',
        ),
    ]