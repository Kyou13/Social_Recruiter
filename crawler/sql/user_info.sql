-- DROP TABLE IF EXISTS social_recruit.user_info

CREATE TABLE IF NOT EXISTS social_recruit.user_info (
            user_id BIGINT,
            screen_name TEXT,
            location TEXT,
            url TEXT,
            discription TEXT,
            friends_count INT,
            followers_count INT,
            listed_count INT,
            favourites_count INT,
            statuses_count INT,
            created_at TIMESTAMP WITH TIME ZONE,
            PRIMARY KEY(user_id)
        )