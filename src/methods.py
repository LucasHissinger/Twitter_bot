##
## PERSONAL PROJECT, 2022
## bot
## File description:
## methods
##

import time
from create_img import create_img, read_and_set
from utils import *
from anime import *
import requests
import csv
import os
import wget
from googletrans import Translator
import datetime

def tweet(api, dt_now, output):
    if dt_now.strftime("%H:%M:%S") >= "15:04:00" and dt_now.strftime("%H:%M:%S") <= "15:04:14":
        output.write(str(datetime.datetime.now()) + " TWEET!\n")
        create_img()
        media = api.media_upload("final_img.png")
        tweet = "Daily post"
        api.update_status(status=tweet, media_ids=[media.media_id])
        os.remove("final_img.png")

def coiffeur(api, tweet, output):
    string = tweet.text[::-1]
    tmp = ""
    for i in range(len(string)):
        if string[i].isalpha():
            tmp += string[i]
        if len(tmp) == 4: break
    if tmp[::-1].lower() == 'quoi':
        output.write(str(datetime.datetime.now()) + " coiffeur reply\n")
        response = response = "@" + tweet.user.screen_name + " Feur"
        api.update_status(status=response, in_reply_to_status_id=tweet.id)
    elif 'quoi' in tweet.text.lower():
        response = response = "@" + tweet.user.screen_name + " Je pense que feur"
        api.update_status(status=response, in_reply_to_status_id=tweet.id)
        output.write(str(datetime.datetime.now()) + " coiffeur reply\n")

def anime(api, tweet, output):
    if '#anime' in tweet.text.lower():
        output.write(str(datetime.datetime.now()) + " anime reply\n")
        link = anime_main(tweet.text)
        if link == "$ERROR$":
            api.update_status(status="@" + tweet.user.screen_name + " Je ne connais pas cet animé :(\n N'hesitez pas a m'en faire part dans mes DM", in_reply_to_status_id=tweet.id)
            return;
        media = api.media_upload("anime_syn.png")
        api.update_status(status="@" + tweet.user.screen_name + " for more info : " + link, in_reply_to_status_id=tweet.id, media_ids=[media.media_id])
        os.remove("anime_syn.png")

def reply(api, output):
    num_tweet = 0
    tweets = api.mentions_timeline(count=10)
    with open("../txt/last_seen.txt", "r") as f:
        content = f.readlines()
    tmp = open("../txt/tmp.txt", "a")
    time.sleep(13)
    output.write(25*"=" + " " + str(datetime.datetime.now()) + " " + 25*"=" + "\n")
    for tweet in (tweets):
        id = read_last_id(num_tweet)
        if str(tweet.id) + "\n" in content:
            store_last_id(tweet.id, tmp)
        elif (id != str(tweet.id)):
            output.write(str(datetime.datetime.now()) + " new tweet : " + tweet.text + " by : " + tweet.user.screen_name + "\n")
            # message_dm(api, tweet, output)
            # get_meteo(api, tweet, output)
            # anime(api, tweet, output)
            # show_help(api, tweet, output)
            # coiffeur(api, tweet, output)
            # try:
            #     api.create_favorite(tweet.id)
            #     print("liked")
            # except Exception as e:
            #     pass
            store_last_id(tweet.id, tmp)
        num_tweet += 1
    tmp.close()
    os.remove("../txt/last_seen.txt")
    os.rename("../txt/tmp.txt", "../txt/last_seen.txt")

def message_dm(api, tweet, output):
    if '#dm' in tweet.text.lower():
        output.write(str(datetime.datetime.now()) + " DM reply !\n")
        message = read_and_set('../txt/citations_life.txt')
        message += "\nby : me :)"
        api.send_direct_message(tweet.user.id, message)

def show_help(api, tweet, output):
    if '#help' in tweet.text.lower():
        output.write(str(datetime.datetime.now()) + " help reply !\n")
        message = ""
        with open("../txt/help.txt", encoding='utf-8') as f:
            message = f.read()
        f.close()
        api.send_direct_message(tweet.user.id, message)
        response = "@" + tweet.user.screen_name + " Check your DM now ! :D"
        api.update_status(status=response, in_reply_to_status_id=tweet.id)

def get_meteo(api, tweet, output):
    if '#meteo' in tweet.text.lower():
        output.write(str(datetime.datetime.now()) + " meteo reply\n")
        ville = get_city(tweet.text)
        if ville == "84":
            api.update_status(status="@" + tweet.user.screen_name + " Je ne connais pas cette ville :(\n Vous êtes sûr de l'orthographe ?", in_reply_to_status_id=tweet.id)
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
        temps = data['weather'][0]['description']
        message += "\nConditions climatiques : " +  Translator().translate(str(temps), dest='fr').text
        api.update_status(status="@" + tweet.user.screen_name + " " + message, in_reply_to_status_id=tweet.id)