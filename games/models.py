from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models

def developers_path(instance, filename):
    return 'developers/{0}/{1}'.format(instance.slug, filename)

def publisher_path(instance, filename):
    return 'publishers/{0}/{1}'.format(instance.slug, filename)

def games_box_art_path(instance, filename):
    return 'box_arts/{0}/{1}'.format(instance.slug, filename)

class PLATFORM(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(unique=True, max_length = 100)

    def __str__(self):
        return '{}'.format(self.title)

class DEVELOPER(models.Model):
    title = models.CharField(max_length = 50)
    about = models.TextField()
    logo =  models.FileField(upload_to = developers_path)
    slug = models.SlugField(unique=True, max_length = 100)

    def __str__(self):
        return '{}'.format(self.title)

class PUBLISHER(models.Model):
    title = models.CharField(max_length = 50)
    about = models.TextField()
    logo =  models.FileField(upload_to = publisher_path)
    slug = models.SlugField(unique=True, max_length = 100)

    def __str__(self):
        return '{}'.format(self.title)

class GENRE(models.Model):
    title = models.CharField(max_length = 50)
    about = models.TextField()
    slug = models.SlugField(unique=True, max_length = 100)

    def __str__(self):
        return '{}'.format(self.title)

class GAME(models.Model):
    title = models.CharField(max_length = 50)
    release_date = models.DateTimeField(null = True, blank = True)
    box_art = models.FileField(upload_to = games_box_art_path)
    slug = models.SlugField(unique=True, max_length = 100)
    genre = models.ManyToManyField(GENRE)
    developer = models.ManyToManyField(DEVELOPER)
    publisher = models.OneToOneField(PUBLISHER, on_delete = models.CASCADE)
    platforms = models.ManyToManyField(PLATFORM)
    RATINGESRB = [
        ('EVERYONE', 'همه کس'),
        ('EVERYONE10PLUS', 'همه کس +10'),
        ('TEEN', 'نوجوان'),
        ('MATURE17PLUS', 'بالغ +17'),
        ('ADULTSONLY', 'بزرگ سالان'),
        ('RATINGPENDING', 'در انتظار'),
    ]
    Age_rating = models.CharField(max_length = 45,
    choices = RATINGESRB, default = 'RATINGPENDING')

    def __str__(self):
        return '{}'.format(self.title)
