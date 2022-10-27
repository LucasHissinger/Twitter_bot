##
## PERSONAL PROJECT, 2022
## bot
## File description:
## methods
##

from secrets import choice
import random
import time
from create_img import create_img, read_and_set
from utils import *
from anime import *
import requests
import os
from googletrans import Translator
import datetime

random_minute_retweet = random.randint(0, 59)
random_minute_tweet = random.randint(0, 59)



class Twitter_bot:

    global output
    global dt_now

    def __init__(self, api, status):
        self.api = api
        self.status = status

    def __repr__(self) -> str:
        return f"Twitter_bot({self.api}) and status : {self.status}"

    def tweet(self):
        global random_minute_tweet
        random_minute_tweet = random_min(self.dt_now, random_minute_tweet)
        print("random minute tweet : " + str(random_minute_tweet))
        if self.dt_now.strftime("%H") == "09" and self.dt_now.strftime("%M") == random_minute_tweet and self.dt_now.strftime("%S") > "00" and self.dt_now.strftime("%S") < "14":
            self.get_meteo("#meteo " + random.choice(get_cities("FR", 150000)), 0, "Nobody", False)
        if self.dt_now.strftime("%H") == "15" and int(self.dt_now.strftime("%M")) == random_minute_tweet and self.dt_now.strftime("%S") >= "00" and self.dt_now.strftime("%S") < "14":
            self.output.write(str(datetime.datetime.now()) + " TWEET!\n")
            create_img()
            media = self.api.media_upload("final_img.png")
            tweet = "Daily post"
            self.api.update_status(status=tweet, media_ids=[media.media_id])
            os.remove("final_img.png")

    def coiffeur(self, tweet):
        string = tweet.full_text[::-1]
        tmp = ""
        for i in range(len(string)):
            if string[i].isalpha():
                tmp += string[i]
            if len(tmp) == 4: break
        if tmp[::-1].lower() == 'quoi':
            self.output.write(str(datetime.datetime.now()) + " coiffeur reply\n")
            response = response = "@" + tweet.user.screen_name + " Feur"
            self.api.update_status(status=response, in_reply_to_status_id=tweet.id)
        elif 'quoi' in tweet.full_text.lower():
            response = response = "@" + tweet.user.screen_name + " Je pense que feur"
            self.api.update_status(status=response, in_reply_to_status_id=tweet.id)
            self.output.write(str(datetime.datetime.now()) + " coiffeur reply\n")

    def anime(self, tweet):
        if '#anime' in tweet.full_text.lower():
            self.output.write(str(datetime.datetime.now()) + " anime reply\n")
            link = anime_main(tweet.full_text)
            if link == "$ERROR$":
                self.api.update_status(status="@" + tweet.user.screen_name + " Je ne connais pas cet animé :(\n N'hesitez pas a m'en faire part dans mes DM", in_reply_to_status_id=tweet.id)
                return;
            media = self.api.media_upload("anime_syn.png")
            self.api.update_status(status="@" + tweet.user.screen_name + " for more info : " + link, in_reply_to_status_id=tweet.id, media_ids=[media.media_id])
            os.remove("anime_syn.png")

    def message_dm(self, tweet):
        if '#dm' in tweet.full_text.lower():
            self.output.write(str(datetime.datetime.now()) + " DM reply !\n")
            message = read_and_set('txt/citations_life.txt')
            message += "\nby : me :)"
            self.api.send_direct_message(tweet.user.id, message)

    def show_help(self, tweet):
        if '#help' in tweet.full_text.lower():
            self.output.write(str(datetime.datetime.now()) + " help reply !\n")
            message = ""
            with open("txt/help.txt", encoding='utf-8') as f:
                message = f.read()
            f.close()
            self.api.send_direct_message(tweet.user.id, message)
            response = "@" + tweet.user.screen_name + " Check your DM now ! :D"
            self.api.update_status(status=response, in_reply_to_status_id=tweet.id)

    def get_meteo(self, tweet_text, tweet_id, tweet_user, is_reply):
        if '#meteo' in tweet_text.lower():
            self.output.write(str(datetime.datetime.now()) + " meteo reply\n")
            ville = get_city(tweet_text)
            if ville == "84" and is_reply == True:
                self.api.update_status(status="@" + tweet_user + " Je ne connais pas cette ville :(\n Vous êtes sûr de l'orthographe ?", in_reply_to_status_id=tweet_id)
                print("in reply error")
                return;
            elif ville == "84" and is_reply == False:
                self.output.write(str(datetime.datetime.now()) + "didn't find city\n")
                print("not reply error")
                return;
            url_weather = os.getenv('URL_METEO') + ville + os.getenv('API_METEO')
            r_weather = requests.get(url_weather)
            data = r_weather.json()
            message = "Vous etes a " + ville
            t = data['main']['temp']
            message += "\nLa temperature moyenne est de " + str(round(t - 273.15, 2)) + " degres Celsius"
            t_min = data['main']['temp_min']
            t_max = data['main']['temp_max']
            message += "\nLes temperatures varient entre " + str(round(t_min - 273.15, 2)) + " et " + str(round(t_max - 273.15, 2)) + " degres Celsius"
            humidite = data['main']['humidity']
            message += "\nLe taux d'humidite est de " + str(humidite) + "%"
            condition = data['weather'][0]['description']
            message += "\nConditions climatiques : " +  Translator().translate(str(condition), dest='fr').text
            if is_reply == True:
                self.api.update_status(status="@" + tweet_user + " " + message, in_reply_to_status_id=tweet_id)
            elif is_reply == False:
                self.output.write(str(datetime.datetime.now()) + " daily post meteo morning\n")
                response = make_reponse(t, humidite)
                final = message + "\n\n" + response
                self.api.update_status(status=final)

    def get_trends_and_retweets(self):
        global random_minute_retweet
        random_minute_retweet = random_min(self.dt_now, random_minute_retweet)
        print("random minute retweet : " + str(random_minute_retweet))
        if self.dt_now.strftime("%H:%M:%S") >= "09:00:00" and self.dt_now.strftime("%H:%M:%S") <= "22:00:00" and int(self.dt_now.strftime("%M")) == random_minute_retweet and self.dt_now.strftime("%S") >= "00" and self.dt_now.strftime("%S") < "14":
                if (random.randint(0, 1) == 1):
                    try :
                        choices = ["Anime", "Jeux vidéos", "League of Legends", "Series", "Information", "crypto", "Informatique", "Twitch", "Gaming", "Films", "Genshin Impact",
                                    "Overwatch", "Wankil", "Youtube", "Amixem", "Cats"]
                        trend = choice(choices)
                        new = self.api.search_tweets(q=trend, count=1, result_type='popular')
                        self.output.write(str(datetime.datetime.now()) + " trends and retweets with this trend : " + str(trend) + "\n")
                        if new == []:
                            new = self.api.search_tweets(q=trend, count=1, result_type='recent')
                            for tweet in new:
                                self.api.create_favorite(tweet.id)
                        else:
                            for tweet in new:
                                self.api.retweet(tweet.id)
                    except Exception as e:
                        self.output.write(str(datetime.datetime.now()) + " already retweet or already liked\n")
                        self.output.write(str(datetime.datetime.now()) + str(e) + "\n")
                        pass
        else:
            pass

    def reply(self):
        num_tweet = 0
        tweets = self.api.mentions_timeline(count=10, tweet_mode = "extended")
        with open("txt/last_seen.txt", "r") as f:
            content = f.readlines()
        tmp = open("txt/tmp.txt", "a")
        time.sleep(13)
        if str(datetime.datetime.now().strftime("%M")) == "00" and (int(datetime.datetime.now().strftime("%S")) >= 00 and int(datetime.datetime.now().strftime("%S")) < 14):
            self.output.write(25*"=" + " " + str(datetime.datetime.now()) + " " + 25*"=" + "\n")
        for tweet in (tweets):
            id = read_last_id(num_tweet)
            if str(tweet.id) + "\n" in content:
                store_last_id(tweet.id, tmp)
            elif (id != str(tweet.id)):
                self.output.write(str(datetime.datetime.now()) + " new tweet : " + tweet.full_text + " by : " + tweet.user.screen_name + "\n")
                self.message_dm(tweet)
                self.get_meteo(tweet.full_text, tweet.id, tweet.user.screen_name, True)
                self.anime(tweet)
                self.show_help(tweet)
                self.coiffeur(tweet)
                try:
                    self.api.create_favorite(tweet.id)
                except Exception as e:
                    pass
                store_last_id(tweet.id, tmp)
            num_tweet += 1
        tmp.close()
        os.remove("txt/last_seen.txt")
        os.rename("txt/tmp.txt", "txt/last_seen.txt")