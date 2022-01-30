import tweepy as tw
from decouple import config


def twitter_authentication():
    auth = tw.OAuthHandler(consumer_key=config('TWITTER_API_KEY'), consumer_secret=config('TWITTER_API_KEY_SECRET'))
    auth.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))
    api = tw.API(auth, wait_on_rate_limit=True)
    return api
