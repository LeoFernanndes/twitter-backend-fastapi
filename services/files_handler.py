import os
from pathlib import Path
import pandas as pd

from tweets.dto import TweetDto
from typing import List

def save_local_user_tweets_csv(user_screen_name: str, tweets_list: List[TweetDto]) -> None:
    parsed_list = [tweet.__dict__ for tweet in tweets_list]
    dataframe = pd.DataFrame(parsed_list)
    local_dir = os.curdir


  
    path = Path(local_dir)
    print(f'{path.parent.absolute()}/local_files/downloaded_csv/{user_screen_name}.csv')    
    dataframe.to_csv(f'{path.parent.absolute()}/local_files/downloaded_csv/{user_screen_name}.csv',index=False)