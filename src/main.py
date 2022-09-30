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

#login to twitter account api
output = open("output.txt", 'w')
output.write(str(datetime.datetime.now()) + " Starting bot...\n")
time.sleep(1)
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)
output.write(str(datetime.datetime.now()) + " CONNECTED\n")
bot = Twitter_bot(api, "online")
output.write("Bot status : " + bot.status + "\n")
output.close()

while True:
    bot.status = "online"
    bot.output = open("output.txt", 'a', encoding="utf-8")
    bot.dt_now = datetime.datetime.now()
    try:
        bot.tweet()
        bot.get_trends_and_retweets()
        bot.reply()
    except tp.errors.TooManyRequests:
        bot.output.write(str(bot.dt_now) + " Too many requests\n")
        bot.status = "offline"
        time.sleep(900)
    except KeyboardInterrupt:
        bot.output.write("exiting safe")
        bot.output.close()
        exit(0)
    except tp.errors.TweepyException:
        bot.status = "offline"
        bot.output.write("Connection closed, bot status :" + bot.status + "\n")
        bot.output.close()
        time.sleep(60)
        bot.output = open("output.txt", 'a', encoding="utf-8")
        bot.status = "online"
        bot.output.write("Connection re-established, bot status :" + bot.status + "\n")
        bot.output.close()
    bot.output.close()
