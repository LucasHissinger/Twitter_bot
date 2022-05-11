##
## PERSONAL PROJECT
## bot
## File description:
## main
##

import tweepy as tp
import time
import os
from create_img import create_img

def tweet():
    create_img()
    media = api.media_upload("final_img.png")
    tweet = ""
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])


# credentials to login to twitter api
consumer_key = 'HgUB4mNQtr3qCfA1UAEAlxGVt'
consumer_secret = 'jXOeZ5UFOwzcxYo4Uu8qJTxaHfsst0our8DxeXvD61k4WUIbXD'
access_token = '1524371703564050437-nNHURCpXJEz33rfuInhss4apXYOHZp'
access_secret = 'XpyKkhsCVXdaA0ypNDolBX72Bo09y3qkyAqbdGd74hvcf'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

while True:
    print("TWEET!")
    tweet()
    time.sleep(60)
