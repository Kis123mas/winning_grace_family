# Generated by Django 4.1.4 on 2022-12-31 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=155, null=True)),
                ('theme', models.TextField(blank=True, max_length=155, null=True)),
                ('date_created', models.DateTimeField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('request', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, max_length=200, null=True)),
                ('title1', models.CharField(blank=True, max_length=200, null=True)),
                ('testimony', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=155)),
                ('post_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('blog_img', models.ImageField(null=True, upload_to='images')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modefied', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='profile2.png', null=True, upload_to='')),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('middlename', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(blank=True, choices=[('Hebrew Women', 'Hebrew Women'), ('Excellent Men', 'Excellent Men'), ('Great Youth', 'Great Youth'), ('Eminence Children', 'Eminence Children')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
