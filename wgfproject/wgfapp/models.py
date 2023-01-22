from django.db import models
from django.contrib.auth.models import User
import uuid
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Member(models.Model):
    CATEGORY = (
        ('Hebrew Women', 'Hebrew Women'), 
        ('Excellent Men', 'Excellent Men'),
        ('Great Youth', 'Great Youth'),
        ('Eminence Children', 'Eminence Children'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="profile2.png", null=True, blank=True)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    middlename = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    twitter_profile = models.CharField(max_length=200, null=True, blank=True)
    facebook_profile = models.CharField(max_length=200, null=True, blank=True)
    instagram_profile = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, choices=CATEGORY, blank=True) 
    date_created = models.DateTimeField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.firstname) + ' | ' + str(self.department)



class Prayer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    request = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Testimony(models.Model):
    name1 = models.CharField(max_length=200, null=True, blank=True)
    title1 = models.CharField(max_length=200, null=True, blank=True)
    testimony = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title1)


class Post(models.Model):
    title = models.CharField(max_length=155)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    blog_img = models.ImageField(upload_to='images', null=True, blank=True)
    body = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    modefied = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post) + ' | ' + str(self.name)




class Event(models.Model):
    host = models.CharField(max_length=155, blank=True, null=True)
    theme = models.TextField(max_length=155, blank=True, null=True)

    date_created = models.DateTimeField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.theme)