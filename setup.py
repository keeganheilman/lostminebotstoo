import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = psycopg2.connect(dbname='postgres',
      user=self.user_name, host='',
      password=self.password)

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 

cur = con.cursor()

cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(self.db_name))
    )






CREATE TABLE account (
    account_id SMALLINT UNSIGNED,
    account_name VARCHAR(280),
    created_at TIMESTAMP WITH TIME ZONE,
    CONSTRAINT pk_account PRIMARY KEY (account_id),
);


CREATE TABLE tweet (
    tweet_id SMALLINT,
    account_id SMALLINT,
    text VARCHAR(280),
    tweeted_at TIMESTAMP WITH TIME ZONE,
    CONSTRAINT pk_tweet PRIMARY KEY (tweet_id),
    CONSTRAINT fk_tweet_account_id FOREIGN KEY (account_id)
    REFERENCES account (account_id)
);


INSERT INTO account (account_id, account_name, created_at) VALUES (1,'@nameofuser', NOW());
INSERT INTO tweet (tweet_id, account_id, text, tweeted_at) VALUES (1,1,'something here.', NOW());



SELECT tweet.text, account.account_name
FROM tweet
JOIN account ON (tweet.account_id = account.account_id);

