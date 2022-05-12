##
## PERSONAL PROJECT
## bot
## File description:
## main
##

import tweepy as tp
import time
import datetime
import os
from create_img import create_img

def tweet(dt_now):
    if now.strftime("%H:%M:%S") == "14:00:30":
        print("TWEET!")
        create_img()
        media = api.media_upload("final_img.png")
        tweet = ""
        post_result = api.update_status(status=tweet, media_ids=[media.media_id])
        time.sleep(1)

def reply():
    print("reply")
    tweets = api.mentions_timeline(1, tweet_mode = 'extended')
    for tweet in tweets:
        #api.update_status(status="@" + tweet.user.screen_name + " " + "Hello I'm a bot in development", in_reply_to_status_id=tweet.id)
        print(str(tweet.id) + ' - ' + tweet.text)


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
    now = datetime.datetime.now()
    tweet(now)
    # reply()
