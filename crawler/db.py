# DBのセットアップ用スクリプト
import os
import psycopg2

class psql_save(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="my_db",
            port="5432",
            user="rui",
            password="password"
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def insert_user_info(self, user):
        col_num = 11
        tmp = ', '.join(['%s' for _ in range(col_num)])
        self.cursor.execute(
            '''INSERT INTO social_recruit.user_info VALUES ({0})'''.format(tmp),
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