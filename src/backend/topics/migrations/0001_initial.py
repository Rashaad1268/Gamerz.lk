# Generated by Django 4.1.1 on 2022-09-16 15:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='topic/images')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='topic/banners')),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='topics.topictag')),
            ],
        ),
    ]
