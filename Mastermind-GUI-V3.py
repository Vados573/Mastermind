from tkinter import *
from tkinter import messagebox
import random


class Line:
    def __init__(self, row):
        self.list = row


class Board:
    def __init__(self, n, m):
        self.__n = n
        self.__m = m
        self.__t = []
        self.row = 0
        self.column = 0
        self.list_final = []
        self.currentlist = []
        for _ in range(n):
            ligne = []
            for _ in range(m):
                ligne.append(0)
            self.__t.append(ligne)

    def display_board(self):
        for i in range(self.__n):
            for j in range(self.__m):
                print(self.__t[i][j], end='\t')
            print()

    def play(self, input):
        self.__t[self.row - 1][self.column] = input
        self.column += 1

    def adjust_column(self):
        self.column = 0

    def check(self, input_line, last_line):
        """Check the sequence of colors that the user inputs"""
        checker = []
        for e in range(4):
            checker.append(last_line[e])
        red = 0
        white = 0
        for n in range(4):
            if input_line[n] == checker[n]:
                red += 1
                checker[n] = -1
                input_line[n] = -2
        for n in range(4):
            if input_line[n] in checker:
                white += 1
                for z in range(4):
                    if checker[z] == input_line[n]:
                        checker[z] = -1
                        break
        black = 4 - (white + red)
        print(white, red, black)
        display_checker(white, red, black)
        if red == 4:
            display_final()
            messagebox.showinfo("Game Over", "Congratulations, you win")
            exit()
        elif self.row == 10:
            display_final()
            messagebox.showinfo("Game Over", "Sorry, you lose")
            exit()

    def generate_code(self):
        """Create the sequence of colors to be found by the player"""
        for _ in range(4):
            random_color = random.randint(0, 5)
            self.list_final.append(random_color)

    def get_code(self):
        return self.list_final

    def get_board(self):
        print(self.row)
        return self.__t[self.row - 1]


def erase():
    for n in range(len(game.currentlist)):
        game_board.delete(game.currentlist[n])
        game.column = 0


def restart():
    game_board.delete("all")
    final.delete("all")
    game.list_final = []
    game.generate_code()
    print(game.get_code())
    game.row = 0
    game.column = 0


def testline():
    if game.column == 4:
        game.check(game.get_board(), game.get_code())
        print("test row")
        game.adjust_column()
        game.currentlist = []
        game.row += 1


def display_final():
    for n in range(4):
        if game.list_final[n] == 0:
            color = "green"
        if game.list_final[n] == 1:
            color = "blue"
        if game.list_final[n] == 2:
            color = "orange"
        if game.list_final[n] == 3:
            color = "red"
        if game.list_final[n] == 4:
            color = "yellow"
        if game.list_final[n] == 5:
            color = "purple"
        final.create_oval(80 + n * 60, 20, 130 + n * 60, 70, fill=color)


def display_checker(w, r, b):
    cnt = 0
    for _ in range(b):
        game_board.create_oval(290 + cnt * 25, 70 + game.row * 60, 310 + cnt * 25, 90 + game.row * 60,
                               fill="black")
        cnt += 1
    for _ in range(r):
        game_board.create_oval(290 + cnt * 25, 70 + game.row * 60, 310 + cnt * 25, 90 + game.row * 60,
                               fill="red")
        cnt += 1
    for _ in range(w):
        game_board.create_oval(290 + cnt * 25, 70 + game.row * 60, 310 + cnt * 25, 90 + game.row * 60,
                               fill="white")
        cnt += 1


def add_g(*args):
    print("clicked green")
    if game.column != 4:
        oval = game_board.create_oval(20 + game.column * 60, 50 + game.row * 60, 70 + game.column * 60,
                                      100 + game.row * 60,
                                      fill="green")
        game.play(0)
        game.currentlist.append(oval)


def add_b(*args):
    print("clicked blue")
    if game.column != 4:
        oval = game_board.create_oval(20 + game.column * 60, 50 + game.row * 60, 70 + game.column * 60,
                                      100 + game.row * 60,
                                      fill="blue")
        game.play(1)
        game.currentlist.append(oval)


def add_o(*args):
    print("clicked orange")
    if game.column != 4:
        oval = game_board.create_oval(20 + game.column * 60, 50 + game.row * 60, 70 + game.column * 60,
                                      100 + game.row * 60,
                                      fill="orange")
        game.play(2)
        game.currentlist.append(oval)


def add_r(*args):
    print("clicked red")
    if game.column != 4:
        oval = game_board.create_oval(20 + game.column * 60, 50 + game.row * 60, 70 + game.column * 60,
                                      100 + game.row * 60,
                                      fill="red")
        game.play(3)
        game.currentlist.append(oval)


def add_y(*args):
    print("clicked yellow")
    if game.column != 4:
        oval = game_board.create_oval(20 + game.column * 60, 50 + game.row * 60, 70 + game.column * 60,
                                      100 + game.row * 60,
                                      fill="yellow")
        game.play(4)
        game.currentlist.append(oval)


def add_p(*args):
    print("clicked purple")
    if game.column != 4:
        oval = game_board.create_oval(20 + game.column * 60, 50 + game.row * 60, 70 + game.column * 60,
                                      100 + game.row * 60,
                                      fill="purple")
        game.play(5)
        game.currentlist.append(oval)


window = Tk()
game = Board(10, 4)
game.generate_code()
print(game.get_code())
window.title("Mastermind")
window.geometry("600x900")
window.configure(bg="black")
window.resizable(False, False)
Code = Label(window, text=".   .   .   .", bg="black", fg="white")
Code.place(x=150, y=740)
Code.config(font=("Courier", 20))
final = Canvas(window, width="400", height="100", borderwidth="0", bg="black", highlightbackground="white")
final.place(x=75, y=740)
color_choice = Canvas(window, width="450", height="100", bg="black", highlightbackground="black")
color_choice.place(x=80, y=-40)
green_button = color_choice.create_oval(20, 50, 70, 100, fill="green", tags="green_button")
blue_button = color_choice.create_oval(80, 50, 130, 100, fill="blue", tags="blue_button")
orange_button = color_choice.create_oval(140, 50, 190, 100, fill="orange", tags="orange_button")
red_button = color_choice.create_oval(200, 50, 250, 100, fill="red", tags="red_button")
yellow_button = color_choice.create_oval(260, 50, 310, 100, fill="yellow", tags="yellow_button")
purple_button = color_choice.create_oval(320, 50, 370, 100, fill="purple", tags="purple_button")

color_choice.tag_bind("green_button", "<Button-1>", add_g)
color_choice.tag_bind("blue_button", "<Button-1>", add_b)
color_choice.tag_bind("orange_button", "<Button-1>", add_o)
color_choice.tag_bind("red_button", "<Button-1>", add_r)
color_choice.tag_bind("yellow_button", "<Button-1>", add_y)
color_choice.tag_bind("purple_button", "<Button-1>", add_p)

game_board = Canvas(window, width="400", height="650", borderwidth="0", bg="gray", highlightbackground="gray")
game_board.place(x=75, y=80)


def chosen_color():
    color1 = Label(window, text="")
    color1.place()


Main_frame = Frame(window)
Main_frame.pack()

erase_but = Button(window, text="Erase Line", padx="10", command=erase)
erase_but.place(x=494, y=380)

test_but = Button(window, text="Test the Line", padx="3", command=testline)
test_but.place(x=494, y=430)

restart_but = Button(window, text="Restart", padx="3", command=restart)
restart_but.place(x=494, y=480)

window.mainloop()
