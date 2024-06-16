from tkinter import *
import pandas
from random import choice, randint

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# __________________________________READ FROM FILE/ _____________________________________#
# data = pandas.DataFrame(data_file)
try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
    to_learn = data_file.to_dict("records")
except FileNotFoundError:
    data_file = pandas.read_csv("data/Korean flash cards - Sheet1.csv")
    to_learn = data_file.to_dict("records")

# __________________________________ FLASH CARD FUNCTIONING _____________________________________#


def next_word():
    global to_learn, current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_background, image=front_img)
    canvas.itemconfig(title_label, text="Korean", fill="black")
    canvas.itemconfig(word, text=current_card["korean"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=back_img)
    canvas.itemconfig(title_label, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["english"], fill="white")


def known():
    global to_learn
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def unknown():
    next_word()

# __________________________________UI_____________________________________#


window = Tk()
window.title("Cardy Cardy Flash Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
current_card = choice(to_learn)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)
title_label = canvas.create_text(400, 150, text="Korean", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=f"{current_card['korean']}", font=("Ariel", 60, "bold"))

# BUTTONS
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=unknown)
wrong_button.grid(column=0, row=1)

# Labels


window.mainloop()

