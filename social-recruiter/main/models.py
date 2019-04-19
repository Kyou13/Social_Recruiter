from django.db import models
from django.contrib.auth import get_user_model

class UserInfo(models.Model):
  id = models.BigIntegerField(primary_key=True)
  name = models.TextField(blank=True, null=True)
  screen_name = models.TextField(blank=True, null=True)
  location = models.TextField(blank=True, null=True)
  url = models.TextField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  follows_count = models.IntegerField(blank=True, null=True)
  followers_count = models.IntegerField(blank=True, null=True)
  listed_count = models.IntegerField(blank=True, null=True)
  favourites_count = models.IntegerField(blank=True, null=True)
  tweets_count = models.IntegerField(blank=True, null=True)
  created_at = models.DateTimeField(blank=True, null=True)
  like_num = models.IntegerField(default=0)

  class Meta:
    # table作らないオプション
    managed = False
    db_table = 'user_info'


class Like(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='like_user')
  twitter_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)
