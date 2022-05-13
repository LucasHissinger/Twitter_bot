##
## PERSONAL PROJECT, 2022
## bot
## File description:
## methods
##

import time
import tweepy as tp
from create_img import create_img

def read_last_id():
    file = open("txt/last_id.txt", "r")
    last_id = int(file.read().strip())
    file.close()
    return last_id

def store_last_id(last_id):
        file = open("txt/last_id.txt", "w")
        file.write(str(last_id))
        file.close()
        return;

def tweet(api, dt_now):
    if dt_now.strftime("%H:%M:%S") == "14:30:00":
        print("TWEET!")
        create_img()
        media = api.media_upload("final_img.png")
        tweet = "Daily post"
        post_result = api.update_status(status=tweet, media_ids=[media.media_id])
        time.sleep(1)

def reply(api):
    #tweets = api.mentions_timeline(read_last_id(), tweet_mode = 'extended')
    tweets = api.mentions_timeline()
    # for tweet in reversed(tweets):
    for tweet in tweets:
        if '#bot' in tweet.text.lower():
            print(str(tweet.id) + " - " + tweet.text)
        #store_last_id(tweet.id)

def message_dm(api, id_user, message):
    api.send_direct_message(id_user, message)
    time.sleep(1)
