  # DBのセットアップ用スクリプト
import os
import psycopg2
from main.models import UserInfo
import datetime

class psql_save(object):
  def __init__(self):
    self.DB_NAME = os.environ.get("DB_NAME")
    self.conn = psycopg2.connect(
      host="localhost",
      database=self.DB_NAME,
      port="5432",
      user=os.environ.get("DB_USER"),
      password=os.environ.get("DB_PASSWORD")
    )
    self.conn.autocommit = True
    # TODO: with使ったやつにしたい
    self.cursor = self.conn.cursor()

  def insert_user_info(self, user):
    try:
      create_date = datetime.datetime.strptime(user['created_at'],'%a %b %d %H:%M:%S %z %Y')
      user_info = UserInfo(
        id=user['id'],
        name=user['name'],
        screen_name = user['screen_name'],
        location = user['location'],
        url = user['url'],
        description = user['description'],
        follows_count = user['friends_count'],
        followers_count = user['followers_count'],
        listed_count = user['listed_count'],
        favourites_count = user['favourites_count'],
        tweets_count = user['statuses_count'],
        created_at = create_date
      )
      user_info.save()
    except Exception as e:
      print(str(e))
  # col_num = 12
  # %s, %s,.. という文字列を生成
  # tmp = ', '.join(['%s' for _ in range(col_num)])
  # self.cursor.execute(
  #     '''INSERT INTO user_info("id", "name", "screen_name", "location", "url", "description", "follows_count", "followers_count", "listed_count", "favourites_count", "tweets_count", "created_at") VALUES ({0})'''.format(tmp),
  #     (
  #         user['id'],
  #         user['name'],
  #         user['screen_name'],
  #         user['location'],
  #         user['url'],
  #         user['description'],
  #         user['friends_count'],
  #         user['followers_count'],
  #         user['listed_count'],
  #         user['favourites_count'],
  #         user['statuses_count'],
  #         user['created_at']
  #     )
  # )

  def insert_status(self, user_id, screen_name, status_id, text):
    self.cursor.execute(
      '''INSERT INTO twitter.status_info VALUES (%s, %s, %s, %s)''',
      (
        user_id,
        screen_name,
        status_id,
        text
      )
    )

  # return
  # list[tuple(3)]
  def select_description_all(self):
    self.cursor.execute(
      '''SELECT id, description FROM user_info'''
    )
    return self.cursor.fetchall()


  def close_section(self):
    self.cursor.close()
    self.conn.close()


class RDS:
  def __init__(self):
    self.conn = psycopg2.connect(
      host=os.getenv('RDS_HOST'),
      database=os.getenv('RDS_DATABASE'),
      port="5432",
      user=os.getenv('RDS_USERNAME'),
      password=os.getenv('RDS_PASSWORD')
    )
    self.conn.autocommit = True
    self.cursor = self.conn.cursor()

  def check_conn(self):
    print (self.conn.get_backend_pid())

  def insert_user_info(self, user):
    col_num = 11
    tmp = ', '.join(['%s' for _ in range(col_num)])
    self.cursor.execute(
      '''INSERT INTO twitter_db.user_info VALUES ({0})'''.format(tmp),
      (
        user['id'],
        user['screen_name'],
        user['location'],
        user['url'],
        user['description'],
        user['friends_count'],
        user['followers_count'],
        user['listed_count'],
        user['favourites_count'],
        user['statuses_count'],
        user['created_at']
      )
    )


  def close(self):
    self.cursor.close()
    self.conn.close()

if __name__=='__main__':
  rds = RDS()
  rds.conn_check()
  rds.close()
