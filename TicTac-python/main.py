from tkinter import ttk, Tk, Label, Button, Frame

import random

def next_turn(row,column):
    global player
    if buttons[row][column]['text']=="" and check_winner() is False:
        if player==players[0]:
            buttons[row][column]['text']=player

        if check_winner() is False:
             player=player[1]
             label.config(text=(player[1]+"turn"))

        elif check_winner() is True:
            label.config(text=(player[0]+"win"))
        elif check_winner() == "Tie":
            label.config(text=("It is a Tie"))

    else:
        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = player[0]
            label.config(text=(player[0] + "turn"))

        elif check_winner() is True:
            label.config(text=(player[1] + "win"))
        elif check_winner() == "Tie":
            label.config(text=("It is a Tie"))


def check_winner():
    for row in range(3):
        if buttons[row][column]['text']== buttons[row][1]['text']== buttons[row][2]['text'] != "" :
            return True
        



def new_game():
    pass

window=Tk()
#window.geometry("500x500")
players=["x","o"]
player=random.choice(players)
window.title("Tic Tac" )
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]

label=Label(text=player+"\'s turn",font=('consolas',20))
label.pack(side="top")
reset_button=Button(text="reset",font=('consolas',20),command=new_game)
reset_button.pack(side="top")
frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",width=5,height=2,font=('consolas',40),
                                 command=lambda row=row,column=column:next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)




window.mainloop()
