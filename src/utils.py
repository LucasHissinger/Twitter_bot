##
## PERSONAL PROJECT, 2022
## Twitter_bot
## File description:
## utils
##

import csv
import random

def random_min(now, minutes):
    if now.strftime("%M") == "00" and now.strftime("%S") > "00" and now.strftime("%S") <= "14":
        random_min = random.randint(0, 59)
        if random_min != 30 or random_min != 0:
            return random_min
        elif random_min == 0 or random_min == 30:
            return random_min + 1
    else:
        return minutes

def read_last_id(line):
    file = open("txt/last_seen.txt", "r")
    content = file.readlines()
    file.close()
    return content[line].replace("\n","")

def store_last_id(last_id, file):
    file.write(str(last_id) + "\n")
    return;

def get_city(string):
    file = open("txt/cities.csv", "r", encoding="utf-8")
    data = csv.reader(file, delimiter=',')
    for row in data:
        if row[0] in string:
            return row[0]
    return "84"