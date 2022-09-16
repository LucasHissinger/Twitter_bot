##
## PERSONAL PROJECT
## bot twitter
## File description:
## main
##

import tweepy as tp
import os
import time
import datetime
from dotenv import load_dotenv
from methods import *

load_dotenv()

# credentials to login to twitter api
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')

print("starting bot")
#login to twitter account api
output = open("output.txt", 'w')
output.write(str(now) + " Starting bot...\n")
time.sleep(1)
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)
output.write(str(now) + " CONNECTED\n")
output.close()

while True:
    output = open("output.txt", 'a')
    now = datetime.datetime.now()
    try:
        tweet(api, now, output)
        reply(api, output)
    except tp.errors.TooManyRequests:
        output.write(str(now) + " Too many requests\n")
        print("Limit request reached, waiting 15 minutes")
        time.sleep(900)
    except KeyboardInterrupt:
        output.write("exiting safe")
        output.close()
        exit(0)
    output.close()
