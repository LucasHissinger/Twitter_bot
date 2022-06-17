##
## PERSONAL PROJECT, 2022
## bot
## File description:
## methods
##

import time
import tweepy as tp
from create_img import create_img, read_and_set
from anime import *
import requests
import json
import csv
import os

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
    tweet = 0
    if dt_now.strftime("%H:%M:%S") == "15:19:10":
        tweet = 1
    if tweet == 1:
        print("TWEET!")
        create_img()
        media = api.media_upload("final_img.png")
        tweet = "Daily post"
        api.update_status(status=tweet, media_ids=[media.media_id])
        tweet = 0

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
    elif 'quoi' in tweet.text.lower():
        response = response = "@" + tweet.user.screen_name + " Je pense que feur"
        api.update_status(status=response, in_reply_to_status_id=tweet.id)

def anime(api, tweet):
    if '#anime' in tweet.text.lower():
        link = anime_main(tweet.text)
        if link == "$ERROR$":
            api.update_status(status="@" + tweet.user.screen_name + " Je ne connais pas cet animé :(\n N'hesitez pas a m'en faire part dans mes DM", in_reply_to_status_id=tweet.id)
            return;
        media = api.media_upload("anime_syn.png")
        api.update_status(status="@" + tweet.user.screen_name + " for more info : " + link, in_reply_to_status_id=tweet.id, media_ids=[media.media_id])


def reply(api):
    tweets = api.mentions_timeline(count=1)
    time.sleep(5)
    for tweet in (tweets):
        print("tweet : " + tweet.text + " by : " + tweet.user.screen_name)
        if (read_last_id() != tweet.id):
            print("reply !")
            coiffeur(api, tweet)
            message_dm(api, tweet)
            show_help(api, tweet)
            get_meteo(api, tweet)
            anime(api, tweet)
            api.create_favorite(tweet.id)
            store_last_id(tweet.id)

def message_dm(api, tweet):
    if '#dm' in tweet.text.lower():
        print("DM !")
        message = read_and_set('txt/citations_life.txt')
        message += "\nby : me :)"
        api.send_direct_message(tweet.user.id, message)

def show_help(api, tweet):
    if '#help' in tweet.text.lower():
        print("help !")
        message = ""
        with open("txt/help.txt") as f:
            message = f.read()
        f.close()
        api.send_direct_message(tweet.user.id, message)
        response = "@" + tweet.user.screen_name + " Check your DM now ! :D"
        api.update_status(status=response, in_reply_to_status_id=tweet.id)

def get_city(string):

    file = open("txt/cities.csv", "r")
    data = csv.reader(file, delimiter=',')
    names = []
    for row in data:
        names.append(row[0])
    for name in names:
        if name in string:
            return name
    return "84"

def get_meteo(api, tweet):
    if '#meteo' in tweet.text.lower():
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
        message += "\nConditions climatiques : " + str(temps)
        api.update_status(status="@" + tweet.user.screen_name + " " + message, in_reply_to_status_id=tweet.id)
        time.sleep(1)
