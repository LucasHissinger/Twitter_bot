##
## PERSONAL PROJECT, 2022
## Twitter_bot
## File description:
## utils
##

import csv
import random
import os

sentences = {
    7.5: "Alors aujourd'hui fait attention a pas te transformer en glacon !",
    10: "Il va faire froid aujourd'hui ! glaglagla :(",
    12.5: "Il fait un peu frisquette fait attention a toi mon loulou !",
    15: "Tu vas devoir prendre ton pull aujourd'hui ...",
    17.5: "C'est bon tu peux faire tomber la veste aujourd'hui !",
    20: "Il va faire bon aujourd'hui !",
    22.5: "Bonne nouvelle le thermometre commence a grimper !",
    25: "Il va faire chaud aujourd'hui !",
    27.5: "Pile a l'heure pour sortir le marcel",
    30: "Aujourd'hui tu vas cuire comme un oeuf, fait attention a toi !"
}

humidity = {
    0: "Mais il fait vraiment trop sec.",
    20: "Mais c'est un peu sec.",
    40: "Et niveau humidité on est bien là.",
    60: "Et il commence a bien faire humide là.",
    80: "Il fait tellement humide qu'on se croirait dans la jungle",
    100: "Mais on est train de dégouliner tellement qu'il fait humide."
}

check_values = [sentences, humidity]

def random_min(now, minutes):
    if now.strftime("%M") == "00" and now.strftime("%S") > "00" and now.strftime("%S") <= "13":
        random_min = random.randint(0, 59)
        if random_min != 30 and random_min != 0:
            return random_min
        else:
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

def get_cities(code_pays, nb_habitants):
    cities = []
    file = open("txt/cities.csv", "r", encoding="utf-8")
    data = csv.reader(file, delimiter=',')
    for row in data:
        cities.append(row[0]) if row[5] == code_pays and int(row[9]) > nb_habitants else 0
    return cities

def make_reponse(t, humidite):
    global check_values
    response = ""
    for key in check_values[0]:
        if key > round(t - 273.15, 2):
            response += check_values[0][key - 2.5] + "\n"
            break
    for key in check_values[1]:
        if key > humidite:
            response += check_values[1][key - 20] + "\n"
            break
    return response