##
## PERSONAL PROJECT
## bot
## File description:
## main
##

import tweepy as tp
import os
import time
import datetime
from dotenv import load_dotenv
from create_img import create_img
from methods import *

load_dotenv()

# credentials to login to twitter api
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')
url_anime = 'https://fr.wikipedia.org/wiki/'

#login to twitter account api
print("Starting bot...")
time.sleep(1)
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)
print("CONNECTED")

while True:
    now = datetime.datetime.now()
    tweet(api, now)
    reply(api)
