# Generated by Django 4.1.4 on 2022-12-11 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
