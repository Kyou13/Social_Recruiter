-- DROP TABLE IF EXISTS social_recruit.user_info

CREATE TABLE IF NOT EXISTS user_info (
            id BIGINT,
            name TEXT,
            screen_name TEXT,
            location TEXT,
            url TEXT,
            description TEXT,
            follows_count INT,
            followers_count INT,
            listed_count INT,
            favourites_count INT,
            statuses_count INT,
            created_at TIMESTAMP WITH TIME ZONE,
            PRIMARY KEY(id)
        )

