##
## PERSONNAL PROJECT, 2022
## Twitter_bot
## File description:
## test
##

from ntpath import join
from selenium import webdriver
from time import sleep
from googlesearch import search
import csv

def get_anime(title):

    file = open("txt/animes.csv", "r")
    data = csv.reader(file, delimiter=',')
    names = []
    for row in data:
        names.append(row[1])
    for name in names:
        if title.lower() in name.lower():
            return True
    return False

def get_screen(driver):
    driver.get_screenshot_as_file("anime_syn.png")

def click_on_link(links):
    driver = webdriver.Chrome()
    link = ""
    for url in links:
        if '.wikipedia' in url:
            if url[:10] == 'https://en':
                link = list(url)
                link[8] = 'f'
                link[9] = 'r'
                link = "".join(link)
                break
            else:
                link = url
                break
    if link == "":
        link = links[0]
    print("FINAL LINK : " + link)
    driver.get(link)
    sleep(3)
    get_screen(driver)
    return link

def search_anime(choice):
    choice += ' wkiipedia'
    links = []
    for j in search(choice):
        links.append(j)
    print(links)
    return click_on_link(links)

def parsing(string):
    string = list(string)
    new = ""
    state = 0
    for char in string:
        if char == '#' or char == '@':
            state = 1;
        if state == 0:
            new += char
        if char == ' ':
            state = 0
    return new

def anime_main(choice):
    new = parsing(choice)
    if new[len(new) - 1] == ' ':
        new = new[:len(new) - 1]
    elif new[0] == ' ':
        new = new[1:]
    print("[" + new + "]")
    anime = get_anime(new)
    if anime == False:
        print("Anime non trouvé")
        return "$ERROR$"
    else:
        return search_anime(new)
