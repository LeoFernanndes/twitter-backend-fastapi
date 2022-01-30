import pandas as pd

from tweets.dto import TweetDto
from typing import List

def save_local_user_tweets_csv(user_screen_name: str, tweets_list: List[TweetDto]) -> None:
    parsed_list = [tweet.__dict__ for tweet in tweets_list]
    dataframe = pd.DataFrame(parsed_list)
    dataframe.to_csv(f'/home/ubuntu/twitter_monitor/twitter-worker/local_files/{user_screen_name}.csv',index=False)