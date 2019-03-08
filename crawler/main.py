import psycopg2
import time
import random
import numpy as np
import pandas as pd
import argparse

from functions import twitter

def get_user_info(targets):

    tw = twitter()
    for t in targets:
        ids = tw.getFollowerIds(screen_name=t)
        tw.getUserInfo(ids)
        with open("crawl.log", "a") as f:
          f.write(t+"\n")
        time.sleep(5)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    # 空白区切りでtargetを与える ex. -t "user1 user2 user3"
    parser.add_argument('-t', '--target', help="Target user's screen name", required=True)
    args = parser.parse_args()

    targets = [i for i in args.target.split()]
    get_user_info(targets)
