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
    file = open("txt/last_seen.txt", "r")
    last_id = int(file.read().strip())
    file.close()
    return last_id

def store_last_id(last_id):
        file = open("txt/last_seen.txt", "w")
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

def coiffeur(api, tweet):
    str = tweet.text[::-1]
    tmp = ""
    for i in range(len(str)):
        if str[i].isalpha():
            tmp += str[i]
        if len(tmp) == 4: break
    if tmp[::-1].lower() == 'quoi':
        response = response = "@" + tweet.user.screen_name + " Feur"
        api.update_status(status=response, in_reply_to_status_id=tweet.id)


def reply(api):
    tweets = api.mentions_timeline(count=1)
    for tweet in (tweets):
        if (read_last_id() != tweet.id):
            print("reply !")
            # response = "@" + tweet.user.screen_name + " Thanks for this comment !"
            # api.update_status(status=response, in_reply_to_status_id=tweet.id)=
            api.create_favorite(tweet.id)
            coiffeur(api, tweet)
            store_last_id(tweet.id)
            time.sleep(1)

def message_dm(api, id_user, message):
    api.send_direct_message(id_user, message)
    time.sleep(1)
