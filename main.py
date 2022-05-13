##
## PERSONAL PROJECT
## bot
## File description:
## main
##

import tweepy as tp
import time
import datetime
from create_img import create_img
from methods import *

# credentials to login to twitter api
consumer_key = 'ajAOTvyerVonmUFftOKaqFBOX'
consumer_secret = 'lRi5hZxvX3mRCjX2HEdY58PmrSD2YASoUrUNK2ihejvWzfUiUC'
access_token = '1524371703564050437-Y3TaH9tKvOh93lto0S8VO2eVgBz94c'
access_secret = 'C8GfyxIDahdHCxClwOCPH641SmqgEUJI3N8YNufN1ZveG'
url_anime = 'https://fr.wikipedia.org/wiki/'

# login to twitter account api
print("Starting bot...")
time.sleep(1)
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)
print("CONNECTED")

while True:
    now = datetime.datetime.now()
    tweet(api, now)
    # message_dm(1064939606829920261, "Hello Marjo")
    # reply()
