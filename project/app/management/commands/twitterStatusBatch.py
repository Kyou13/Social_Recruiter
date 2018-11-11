from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialAccount, SocialApp
import os
import sys
from project import settings
sys.path.append(os.path.join(settings.BASE_DIR,'../crawler'))
from functions import twitter
from datetime import datetime


class Command(BaseCommand):
  help = 'Update Twitter Information'

  # メインメソッド
  def handle(self, *args, **options):
    socialAccounts = SocialAccount.objects.all()
    timeNow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


    for socialUser in socialAccounts:
      userId = socialUser.extra_data['id_str']
      tw = twitter()
      userStatus = tw.getSpecifiedUserStatus(userId)
      follows = str(userStatus['friends_count'])
      followers = str(userStatus['followers_count'])
      with open(os.path.join(settings.BASE_DIR,'log',userId + '.txt'),'a') as f:
        f.write(timeNow+','+follows+','+followers+'\n')
