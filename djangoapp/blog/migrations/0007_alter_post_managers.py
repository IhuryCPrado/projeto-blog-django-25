# Generated by Django 5.1.5 on 2025-02-05 21:58

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_excerpt_alter_page_is_published_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('objects_2', django.db.models.manager.Manager()),
            ],
        ),
    ]
