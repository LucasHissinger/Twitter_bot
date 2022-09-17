##
## PERSONAL PROJECT, 2022
## Twitter_bot
## File description:
## utils
##

import csv

def read_last_id(line):
    file = open("../txt/last_seen.txt", "r")
    content = file.readlines()
    file.close()
    return content[line].replace("\n","")

def store_last_id(last_id, file):
    file.write(str(last_id) + "\n")
    return;

def get_city(string):
    file = open("../txt/cities.csv", "r", encoding="utf-8")
    data = csv.reader(file, delimiter=',')
    for row in data:
        if row[0] in string:
            return row[0]
    return "84"