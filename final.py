from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import random


def game(choice):
    user_score = 0
    ai_score = 0
    possible_moves = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_moves)

    if computer_action == "rock":
        if choice == "rock":
            print("You Tie!")
        elif choice == "paper":
            print("You Won!")
            user_score += 1
        else:
            print("You Lost!")
            ai_score += 1
    elif computer_action == "paper":
        if choice == "rock":
            print("You Lost!")
            ai_score += 1
        elif choice == "paper":
            print("You Tie!")
        else:
            print("You Won!")
            user_score += 1
    else:
        if choice == "rock":
            print("You Won!")
            user_score += 1
        elif choice == "paper":
            print("You Lost!")
            ai_score += 1
        else:
            print("You Tie!")

class App:
    def __init__(self, root):
        #setting title
        root.title("Rock, Paper, Scissors!!")
        #setting window size
        width=961
        height=655
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        test = ImageTk.PhotoImage(Image.open("test.png"))
        label = Label(image=test)
        label.pack()



        GButton_620=Button(root)
        GButton_620["bg"] = "#f0f0f0"
        GButton_620["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=28)
        GButton_620["font"] = ft
        GButton_620["fg"] = "#000000"
        GButton_620["justify"] = "center"
        GButton_620["text"] = "Rock"
        GButton_620["relief"] = "raised"
        GButton_620.place(x=30,y=490,width=242,height=89)
        GButton_620["command"] = self.GButton_620_command

        GButton_566=Button(root)
        GButton_566["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        GButton_566["font"] = ft
        GButton_566["fg"] = "#000000"
        GButton_566["justify"] = "center"
        GButton_566["text"] = "Paper"
        GButton_566.place(x=340,y=490,width=242,height=89)
        GButton_566["command"] = self.GButton_566_command

        GButton_245=Button(root)
        GButton_245["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        GButton_245["font"] = ft
        GButton_245["fg"] = "#000000"
        GButton_245["justify"] = "center"
        GButton_245["text"] = "Scissors"
        GButton_245.place(x=640,y=490,width=243,height=89)
        GButton_245["command"] = self.GButton_245_command

        GLabel_210 = Label(root)
        ft = tkFont.Font(family='Times', size=58)
        GLabel_210["font"] = ft
        GLabel_210["fg"] = "#333333"
        GLabel_210["justify"] = "center"
        GLabel_210["text"] = "Choose your hand!"
        GLabel_210.place(x=100, y=60, width=728, height=116)

        GLabel_186=Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_186["font"] = ft
        GLabel_186["fg"] = "#333333"
        GLabel_186["justify"] = "center"
        GLabel_186["text"] = "(Best out of Three)"
        GLabel_186.place(x=400,y=160,width=129,height=30)

    def GButton_620_command(self):
        print ("You chose: Rock")
        game("rock")


    def GButton_566_command(self):
        print ("You chose: Paper")
        game("paper")

    def GButton_245_command(self):
        print ("You chose: Scissors")
        game("scissors")

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
