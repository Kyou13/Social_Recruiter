truncate social_recruiter.app_person;

insert into social_recruiter.app_person 
(
  user_id,
  screen_name,
  location,
  url,
  description,
  friends_count,
  followers_count,
  listed_count,
  favourites_count,
  statuses_count,
  created_at
)

select 
  user_id,
  screen_name,
  location,
  url,
  description,
  friends_count,
  followers_count,
  listed_count,
  favourites_count,
  statuses_count,
  created_at
from twitter_db.user_info;


-- $ psql social_recruiter.app_person -h db-analytics.ckcjfvqfv2nq.ap-northeast-1.rds.amazonaws.com -c "COPY social_recruiter.app_person
-- (
--   user_id,
--   screen_name,
--   location,
--   url,
--   description,
--   friends_count,
--   followers_count,
--   listed_count,
--   favourites_count,
--   statuses_count,
--   created_at
-- ) from stdin with csv HEADER DELIMITER ','" < /Users/louis/Desktop/result.csv