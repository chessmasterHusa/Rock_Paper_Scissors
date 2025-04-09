from tkinter import *
from PIL import Image, ImageTk
import random
import os

fenetre = Tk()

# fenetre.geometry("500x500")

emplacement = os.path.dirname(__file__) + "/"

Profile = {1 : ""}
fenetre["bg"] = "yellow"
fenetre.title("Rock Paper Scissors")

random_image = random.randint(1, 3)

player = 0
computer = 0

score_computer = 0
score_player = 0
score_draw = 0

button_disabled = False

load1 = Image.open(emplacement + "Paper_Player.jpg")
P_P = ImageTk.PhotoImage(load1)
Profile[1] = P_P

load2 = Image.open(emplacement + "Paper_Computer.jpg")
P_C = ImageTk.PhotoImage(load2)
Profile[2] = P_C

load3 = Image.open(emplacement + "Rock_Player.jpg")
R_P = ImageTk.PhotoImage(load3)
Profile[3] = R_P

load4 = Image.open(emplacement + "Rock_Computer.jpg")
R_C = ImageTk.PhotoImage(load4)
Profile[4] = R_C

load5 = Image.open(emplacement + "Scissors_Player.jpg")
S_P = ImageTk.PhotoImage(load5)
Profile[5] = S_P

load6 = Image.open(emplacement + "Scissors_Computer.jpg")
S_C = ImageTk.PhotoImage(load6)
Profile[6] = S_C

load7 = Image.open(emplacement + "unknown.jpg")
unknown = ImageTk.PhotoImage(load7)
Profile[7] = unknown

label_image_computer = Label(fenetre, image=unknown)
label_image_computer.grid(row=2, column=1)
label_image_player = Label(fenetre, image=unknown)
label_image_player.grid(row=3, column=1)

def new_game_event(event):
	new_game()

def new_game():
	global random_image
	global player
	global computer
	global button_disabled
	player = 0
	computer = 0
	label_winner["text"] = ""
	label_winner["bg"] = "yellow"
	random_image = random.randint(1, 3)
	label_image_computer = Label(fenetre, image=unknown)
	label_image_computer.grid(row=2, column=1)
	button_new_game["state"] = NORMAL
	label_image_player = Label(fenetre, image=unknown)
	label_image_player.grid(row=3, column=1)
	button_paper["state"] = NORMAL
	button_rock["state"] = NORMAL
	button_scissors["state"] = NORMAL
	button_new_game["state"] = DISABLED
	button_disabled = False



def Paper_Player_event(event):
	Paper_Player()
def Paper_Player():
	global random_image
	global player
	global computer
	global button_disabled
	player = 1
	computer = random_image
	button_paper["state"] = DISABLED
	button_rock["state"] = DISABLED
	button_scissors["state"] = DISABLED
	button_new_game["state"] = NORMAL
	if not button_disabled:
		print(random_image)
		label_image_player = Label(fenetre, image=P_P)
		label_image_player.grid(row=3, column=1)
		if random_image == 1:
			label_image_computer = Label(fenetre, image=P_C)
			label_image_computer.grid(row=2, column=1)
		elif random_image == 2:
			label_image_computer = Label(fenetre, image=R_C)
			label_image_computer.grid(row=2, column=1)
		elif random_image == 3:
			label_image_computer = Label(fenetre, image=S_C)
			label_image_computer.grid(row=2, column=1)
		results()
	button_disabled = True

def Rock_Player_event(event):
	Rock_Player()
def Rock_Player():
	global random_image
	global player
	global computer
	global button_disabled
	player = 2
	computer = random_image
	button_paper["state"] = DISABLED
	button_rock["state"] = DISABLED
	button_scissors["state"] = DISABLED
	button_new_game["state"] = NORMAL
	if not button_disabled:
		label_image_player = Label(fenetre, image=R_P)
		label_image_player.grid(row=3, column=1)
		if random_image == 1:
			label_image_computer = Label(fenetre, image=P_C)
			label_image_computer.grid(row=2, column=1)
		elif random_image == 2:
			label_image_computer = Label(fenetre, image=R_C)
			label_image_computer.grid(row=2, column=1)
		elif random_image == 3:
			label_image_computer = Label(fenetre, image=S_C)
			label_image_computer.grid(row=2, column=1)
		results()
	button_disabled = True


def Scissors_Player_event(event):
	Scissors_Player()
def Scissors_Player():
	global random_image
	global player
	global computer
	global button_disabled
	player = 3
	computer = random_image
	button_paper["state"] = DISABLED
	button_rock["state"] = DISABLED
	button_scissors["state"] = DISABLED
	button_new_game["state"] = NORMAL
	if not button_disabled:
		label_image_player = Label(fenetre, image=S_P)
		label_image_player.grid(row=3, column=1)
		if random_image == 1:
			label_image_computer = Label(fenetre, image=P_C)
			label_image_computer.grid(row=2, column=1)
		elif random_image == 2:
			label_image_computer = Label(fenetre, image=R_C)
			label_image_computer.grid(row=2, column=1)
		elif random_image == 3:
			label_image_computer = Label(fenetre, image=S_C)
			label_image_computer.grid(row=2, column=1)
		results()
	button_disabled = True

label_winner = Label(fenetre, font=("Comic Sans Ms", 30), bg="yellow")
label_winner.grid(row=1, column=1)

button_paper = Button(fenetre, image=P_P, command=Paper_Player)
button_paper.grid(row=4, column=0)
button_rock = Button(fenetre, image=R_P, command=Rock_Player)
button_rock.grid(row=4, column=1)
button_scissors = Button(fenetre, image=S_P, command=Scissors_Player)
button_scissors.grid(row=4, column=2)

button_new_game = Button(fenetre, text="New game", command=new_game, font=("Comic Sans Ms", 20), state=DISABLED)
button_new_game.grid(row=5, column=1)

label_score_computer = Label(fenetre, text=score_computer, font=("Comic Sans Ms", 40))
label_score_computer.grid(row=2, column=0)
label_score_player = Label(fenetre, text=score_player, font=("Comic Sans Ms", 40))
label_score_player.grid(row=3, column=0)


def results():
	global player
	global computer
	if player == 1:
		if computer == 2:
			win()
		elif computer == 3:
			lose()
		else:
			draw()
	if player == 2:
		if computer == 1:
			lose()
		elif computer == 3:
			win()
		else:
			draw()
	if player == 3:
		if computer == 1:
			win()
		elif computer == 2:
			lose()
		else:
			draw()

# P 1 > C 2
# P 1 < C 3

# P 2 < C 1
# P 2 > C 3

# P 3 > C 1
# P 3 < C 2

def win():
	global score_player
	label_winner["text"] = "YOU WIN !"
	label_winner["fg"] = "green"
	label_winner["bg"] = "white"
	score_player += 1
	label_score_player["text"] = score_player

def lose():
	global score_computer
	label_winner["text"] = "YOU LOSE !"
	label_winner["fg"] = "red"
	label_winner["bg"] = "white"
	score_computer += 1
	label_score_computer["text"] = score_computer

def draw():
	global score_draw
	score_draw += 1
	label_winner["text"] += str(score_draw)
	label_winner["text"] += " DRAW !"
	label_winner["fg"] = "blue"
	label_winner["bg"] = "white"

def reset(event):
	global player
	global computer
	global score_computer
	global score_player
	global score_draw
	player = 0
	computer = 0
	score_computer = 0
	score_player = 0
	score_draw = 0
	label_winner["text"] = ""
	label_score_player["text"] = "0"
	label_score_computer["text"] = "0"

fenetre.bind("<Escape>", lambda x: fenetre.quit())
fenetre.bind("<F2>", reset)
fenetre.bind("<space>", new_game_event)

fenetre.bind("<g>", Paper_Player_event)
fenetre.bind("<G>", Paper_Player_event)
fenetre.bind("<h>", Rock_Player_event)
fenetre.bind("<H>", Rock_Player_event)
fenetre.bind("<j>", Scissors_Player_event)
fenetre.bind("<J>", Scissors_Player_event)

fenetre.mainloop()