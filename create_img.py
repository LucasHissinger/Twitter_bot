##
## PERSONAL PROJECT 2022
## python script to make img
## File description:
## main
##

from PIL import Image, ImageDraw, ImageFont
from random import choice, randint
from os import remove

def read_and_set(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    f.close()
    return choice(lines).rstrip("\n")

def random_coords(txt_id):
    if txt_id == 1:
        x = randint(10, 400)
        y = randint(10, 400)
        return (x, y)
    elif txt_id == 2:
        x = randint(10, 400)
        y = randint(400, 750)
        return (x, y)
    else:
        print("Invalid txt_id")
        exit(0)

def create_img():

    colors_pastel = ['#F9E4D6', '#F5CBE0', '#D4BDE7', '#CEDDEB', '#E8EBD5']
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'black']
    font = ['font/Medium.ttf', 'font/Semi.ttf', 'font/Regular.ttf', 'font/Thin.ttf']
    fnt1 = ImageFont.truetype(choice(font), 55)
    fnt2 = ImageFont.truetype(choice(font), 55)

    question = read_and_set('questions.txt')
    answer = read_and_set('response.txt')
    img = Image.new('RGB', (1920, 1080), color = choice(colors_pastel))
    d = ImageDraw.Draw(img)
    d.text(random_coords(1), question, font=fnt1, fill=choice(colors))
    d.text(random_coords(2), answer, font=fnt2, fill=choice(colors))
    img.save('base_img.png')

    Image1 = Image.open('base_img.png')
    Image1copy = Image1.copy()
    Image2 = Image.open('pic/' + str(randint(1,6)) + '.png')
    Image2copy = Image2.copy()
    Image1copy.paste(Image2copy, (randint(0, 1500), randint(200, 800)))
    Image1copy.save('final_img.png') # save the image
    remove('base_img.png')