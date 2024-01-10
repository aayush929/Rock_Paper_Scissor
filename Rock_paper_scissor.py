from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.configure(background="purple")

rock_image = Image.open("Rock-user.png")
rock_img = ImageTk.PhotoImage(rock_image)
rock_image_comp = Image.open("Rock.png")
rock_img_comp = ImageTk.PhotoImage(rock_image_comp)

paper_image = Image.open("Paper-user.png")
paper_img = ImageTk.PhotoImage(paper_image)
paper_image_comp = Image.open("Paper.png")
paper_img_comp = ImageTk.PhotoImage(paper_image_comp)

scissor_image = Image.open("Scissor-user.png")
scissor_img = ImageTk.PhotoImage(scissor_image)
scissor_image_comp = Image.open("Scissor.png")
scissor_img_comp = ImageTk.PhotoImage(scissor_image_comp)

user_label = Label(root, image=rock_img)
user_label.grid(row=1, column=4)
comp_label = Label(root, image=rock_img_comp)
comp_label.grid(row=1, column=0,)

user_label = Label(root, image=paper_img)
user_label.grid(row=1, column=4)
comp_label = Label(root, image=paper_img_comp)
comp_label.grid(row=1, column=0)

user_label = Label(root, image=scissor_img)
user_label.grid(row=1, column=4)
comp_label = Label(root, image=scissor_img_comp)
comp_label.grid(row=1, column=0)

playerScore = Label(root, text=0, font=100,  fg="black")
computerScore = Label(root, text=0, font=100, fg= "black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

user_indicator = Label(root, font=50, text="USER", bg="purple")
comp_indicator = Label(root, font=50,  text="COMPUTER", bg="purple")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

msg = Label(root, font=50, fg="Black", text="You loose")
msg.grid(row=3, column=2)

#update_message
def updateMessage(x):
    msg['text'] = x

#update_userscore
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

def checkWin(player, computer):
    if player == computer:
        updateMessage ("It's a tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
                updateMessage("You Win")
                updateUserScore()
    else:
        pass
#functions
choices = ["rock", "paper", "scissor"]
def updateChoice(x):
    compChoice: str= choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    #for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x, compChoice)

rock = Button(root, width=20, height=2, text="ROCK", bg="green", fg="black",command=lambda:updateChoice("rock"))
rock.grid(row=2, column=1)  # Move ROCK button down
paper = Button(root, width=20, height=2, text="PAPER", bg="yellow", fg="black", command=lambda:updateChoice("paper"))
paper.grid(row=2, column=2, padx=10)  # Move PAPER button down
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="red", fg="black", command=lambda:updateChoice("scissor"))
scissor.grid(row=2, column=3)  # Move SCISSOR button down




root.mainloop()
