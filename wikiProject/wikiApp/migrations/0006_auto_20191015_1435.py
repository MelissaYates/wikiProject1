# Generated by Django 2.0.6 on 2019-10-15 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0005_auto_20191015_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='article',
        ),
    ]
