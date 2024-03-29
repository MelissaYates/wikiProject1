# Generated by Django 2.0.6 on 2019-10-15 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0003_article_img_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Page',
            new_name='AllWiki',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
