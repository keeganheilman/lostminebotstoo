
DROP TABLE IF EXISTS account;
CREATE TABLE account (
    account_id SMALLINT,
    account_name VARCHAR(15) UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE,
    CONSTRAINT pk_account PRIMARY KEY (account_id));

DROP TABLE IF EXISTS tweet;
CREATE TABLE tweet (
    tweet_id SMALLINT,
    account_id SMALLINT,
    text VARCHAR(280),
    tweeted_at TIMESTAMP WITH TIME ZONE,
    CONSTRAINT pk_tweet PRIMARY KEY (tweet_id),
    CONSTRAINT fk_tweet_account_id FOREIGN KEY (account_id) REFERENCES account (account_id) ON DELETE CASCADE);





