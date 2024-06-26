# Generated by Django 5.0.4 on 2024-04-07 14:04

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_published', models.DateTimeField(verbose_name='date published')),
                ('article_image', models.ImageField(upload_to='images/')),
                ('article_content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('article_slug', models.SlugField()),
            ],
        ),
    ]
