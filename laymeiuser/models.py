from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserExtend(models.Model):
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class UserImage(models.Model):
    user_extend = models.ForeignKey(UserExtend)
    image = models.ImageField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class UserDescription(models.Model):
    user_extend = models.ForeignKey(UserExtend)
    description = models.TextField(max_length=400)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class UserFriend(models.Model):
    user_from = models.ForeignKey(UserExtend, related_name='user_from')
    user_to = models.ForeignKey(UserExtend, related_name='user_to')
    status = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
