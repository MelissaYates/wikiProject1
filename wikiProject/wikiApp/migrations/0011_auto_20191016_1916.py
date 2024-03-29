# Generated by Django 2.0.6 on 2019-10-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0010_relatedarticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgFile', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
