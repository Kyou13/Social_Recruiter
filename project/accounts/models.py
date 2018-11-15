from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from app.models import UserInfo

class SocialUser(AbstractUser):
  # 標準のBaseUserManagerを使う代わりに、UserManagerを使う
  objects = UserManager()

  class Meta(object):
    app_label = 'accounts'

  def get_liked_users(self):
    relations = Relationship.objects.filter(user=self)
    user_id_list = [relation.liked_user.id for relation in relations]
    result = UserInfo.objects.filter(pk__in = user_id_list)
    return result


class Relationship(models.Model):
  user = models.ForeignKey(SocialUser, on_delete=models.DO_NOTHING)
  liked_user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
