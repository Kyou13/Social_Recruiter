import os
from os.path import join, dirname
import json
import time
import random
from tqdm import tqdm

import numpy as np
from db import psql_save, RDS
from requests_oauthlib import OAuth1Session

from dotenv import load_dotenv

class twitter():
    def __init__(self):
        # 環境変数から承認情報を取得
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        CONSUMER_KEY    = os.environ['TWITTER_CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
        ACCESS_TOKEN    = os.environ['TWITTER_ACCESS_TOKEN']
        ACCESS_SECRET   = os.environ['TWITTER_ACCESS_SECRET']
        self.api = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)


    # 特定ユーザーフォロワーidリストを取得
    def getFollowerIds(self, screen_name):
        ids = []
        cursor = -1
        url = 'https://api.twitter.com/1.1/followers/ids.json?'
        params = {'screen_name': screen_name}
        print("targetUser:{}".format(screen_name))

        while cursor != 0 and len(ids)<50000:
            req = self.api.get(url, params=params)
            if req.status_code == 200:
                temp = json.loads(req.text)
                ids.extend(temp['ids'])
                cursor = temp['next_cursor']
                params['cursor'] = temp['next_cursor']
                print('totalGetFollowerNum: {}'.format(len(ids)))
            else:
                print ("Error: %d at getFollowerIds" % req.status_code)
            time.sleep(5*random.uniform(0.5,1.5))
        return ids


    # 特定ユーザーフォローidリストを取得
    def getFriendIds(self, screen_name):
        ids = []
        cursor = -1
        url = 'https://api.twitter.com/1.1/friends/ids.json'
        params = {'screen_name': screen_name}

        while cursor != 0:
            req = self.api.get(url, params=params)
            if req.status_code == 200:
                temp = json.loads(req.text)
                ids.extend(temp['ids'])
                print('totalGetFriendNum: {0}'.format(len(ids)))
                cursor = temp['next_cursor']
                params['cursor'] = temp['next_cursor']
                time.sleep(10*random.uniform(0.5,1.5))
            else:
                print ("Error: %d at getFriendIds" % req.status_code)
        return ids


    # user_idからユーザー情報の取得
    def getUserInfo(self, ids):
        url = 'https://api.twitter.com/1.1/users/lookup.json'
        ids = np.array(ids).astype(str)
        db = psql_save()

        # 100個ずつユーザ情報取得
        for i in tqdm(range(0, len(ids), 100)):
            _ids = ','.join(ids[i:i+100])
            params = {'user_id': _ids}

            req = self.api.get(url, params=params)
            if req.status_code == 200:
                req_text = json.loads(req.text)
                for user in req_text:
                    try:
                        db.insert_user_info(user)
                    except:
                        pass
            else:
                print ("Error: %d at getUserInfo()" % req.status_code)
            time.sleep(2*random.uniform(0.5,1.5))
        db.close_section()


    def getUserStatuses(self, screen_name):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {'screen_name': screen_name, 'count': 100}
        psql = psql_save()

        req = self.api.get(url, params=params)
        if req.status_code == 200:
            req_text = json.loads(req.text)
            for status in req_text:
                try:
                    psql.insert_status(status['user']['id'], status['user']['screen_name'], status['id'], status['text'])
                except Exception as e:
                    print("ERROR:{}".format(e))
                    pass
        else:
            print ("Error: %d at getUserInfo()" % req.status_code)

    def getSpecifiedUserStatus(self, user_id):
        url = 'https://api.twitter.com/1.1/users/show.json'
        params = {'user_id': user_id}

        req = self.api.get(url, params=params)
        res = json.loads(req.text)
        return res


