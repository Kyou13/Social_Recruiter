-- DROP TABLE IF EXISTS social_recruit.status_info

CREATE TABLE IF NOT EXISTS social_recruit.status_info (
            user_id BIGINT,
            screen_name TEXT,
            status_id BIGINT,
            status_text TEXT,
            PRIMARY KEY(status_id)
        )