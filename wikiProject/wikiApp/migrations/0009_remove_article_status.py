# Generated by Django 2.0.6 on 2019-10-16 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0008_remove_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
    ]