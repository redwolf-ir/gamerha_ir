from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models

def game_cover_upload_path(instance, filename):
    if " " in instance.GAME.title:
        instance.title.title.replace(" ", "_")
    return '/'.join([instance.name.title, filename])

def d_logo_upload_path(instance, filename):
    if " " in instance.GAME.title:
        instance.title.title.replace(" ", "_")
    return '/'.join([instance.name.title, filename])

class DEVELOPER(models.Model):
    title = models.CharField(max_length = 50, varbose_name = "توسعه دهنده")
    about = models.TextField()
    logo =  models.FileField(upload_to = d_logo_upload_path,
    keep_orphans = True, verbose_name = 'لوگو')
    slug = models.SlugField(unique=True, max_length = 100)

class PUBLISHER(models.Model):
    title = models.CharField(max_length = 50, varbose_name = "ناشر")
    about = models.TextField()
    logo =  models.FileField(upload_to = d_logo_upload_path,
    keep_orphans = True, verbose_name = 'لوگو')
    slug = models.SlugField(unique=True, max_length = 100)

class GENRE(models.Model):
    title = models.CharField(max_length = 50, varbose_name = "عنوان ژانر")
    about = models.TextField()
    slug = models.SlugField(unique=True, max_length = 100)

    def __unicode__(self):
        return self.title

class GAME(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "عنوان بازی")
    release_date = models.DateTimeField(null = True, blank = True,
    verbose_name="تاریخ انتشار")
    cover = models.FileField(upload_to = game_cover_upload_path, keep_orphans = True,
    verbose_name = 'کاور بازی')
    slug = models.SlugField(unique=True, max_length = 100)
    genre = models.ManyToManyField(GENRE, verbose_name = "سبک بازی")
    developer = models.ManyToManyField(DEVELOPER, verbose_name = "توسعه دهنده")
    publisher = models.OneToOneField(PUBLISHER, verbose_name = "ناشر بازی")
    platforms = models.ManyToManyField(PLATFORMS, verbose_name = "پلتفرم")
    RATINGESRB = [
        (EVERYONE, 'همه کس'),
        (EVERYONE10PLUS, 'همه کس +10'),
        (TEEN, 'نوجوان'),
        (MATURE17PLUS, 'بالغ +17'),
        (ADULTSONLY, 'بزرگ سالان'),
        (RATINGPENDING, 'در انتظار'),
    ]
    Age_rating = models.CharField(max_length = 2,
    choices = RATINGESRB, default = RATINGPENDING)

    def __unicode__(self):
        return self.title
