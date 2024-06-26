# Generated by Django 5.0.4 on 2024-04-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('product_type', models.CharField(max_length=25)),
                ('product_description', models.TextField()),
                ('affiliate_url', models.SlugField(blank=True, null=True)),
                ('product_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
