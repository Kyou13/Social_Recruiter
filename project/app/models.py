from django.db import models

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

  class Meta:
    # table作らないオプション
    managed = False
    db_table = 'user_info'

# class Message(models.Model):
#     message = models.TextField(max_length=10000) #formでtext area
#     user = models.ForeignKey(UserSocialAuth, on_delete=models.SET_NULL, null=True)

# class Introduce(models.Model):
#     user = models.OneToOneField(UserSocialAuth, on_delete=models.SET_NULL, null=True)
#     company_name = models.CharField(max_length=64)
#     recruiter = models.CharField(max_length=32)

