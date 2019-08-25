from django.db import models


# Create your models here.

class MovieInfo(models.Model):
    top = models.IntegerField()
    url = models.CharField(max_length=300)
    url_object_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100, default='')
    play_able = models.CharField(max_length=10, default='', null=True, blank=True)
    star = models.CharField(max_length=10, default='', null=True, blank=True)
    year = models.CharField(max_length=60, default='', null=True, blank=True)
    comments_num = models.CharField(max_length=20, default='', null=True, blank=True)
    country = models.CharField(max_length=20, default='', null=True, blank=True)
    actor = models.CharField(max_length=100, default='', null=True, blank=True)
    movie_type = models.CharField(max_length=40, default='', null=True, blank=True)
    director = models.CharField(max_length=100, default='', null=True, blank=True)
    image = models.CharField(max_length=255, default='', null=True, blank=True)
    image_path = models.CharField(max_length=255, default='', null=True, blank=True)

    def __str__(self):
        return self.url_object_id


class User_list(models.Model):
    user_id = models.CharField(max_length=11, primary_key=True, verbose_name="user_id")
    user_name = models.CharField(max_length=30)
    userpassword = models.CharField(max_length=16)
    usertype = models.CharField(max_length=8, null=True, blank=True, default='user')

    def __str__(self):
        return self.user_id


class User_favorite(models.Model):
    user_id = models.CharField(max_length=11)
    watched = models.BooleanField(default=False)
    url_object_id = models.CharField(max_length=50)


class Comments(models.Model):
    user_id = models.CharField(max_length=11)
    url_object_id = models.CharField(max_length=50)
    comments = models.TextField()
