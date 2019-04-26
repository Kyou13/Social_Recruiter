from django.core.management.base import BaseCommand
from main.models import UserInfo

import psycopg2
import time
import random
import numpy as np
import pandas as pd
import argparse

from .crawler.functions import twitter

def get_user_info(targets):
  tw = twitter()
  for t in targets:
    ids = tw.getFollowerIds(screen_name=t)
    tw.getUserInfo(ids)
    with open("crawl.log", "a") as f:
      f.write(t+"\n")
    time.sleep(60*5)


class Command(BaseCommand):
  def add_arguments(self, parser):
    parser.add_argument('targets', nargs='+')

  def handle(self, *args, **options):
    # 空白区切りでtargetを与える ex. -t "user1 user2 user3"
    targets = options['targets']
    get_user_info(targets)
