# Generated by Django 4.1.4 on 2023-01-03 05:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wgfapp', '0008_alter_post_blog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
