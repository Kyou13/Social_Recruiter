from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from app.models import UserInfo

class User(AbstractUser):
  # 標準のBaseUserManagerを使う代わりに、UserManagerを使う
  objects = UserManager()

  class Meta(object):
    app_label = 'accounts'

  def get_liked_users(self):
    relations = Relationship.objects.filter(user=self)
    return [relation.liked_user for relation in relations]

class Relationship(models.Model):
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  liked_user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
