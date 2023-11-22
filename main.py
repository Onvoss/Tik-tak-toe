from tkinter import *
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")

        self.players = ["X", "O"]
        self.player = random.choice(self.players)

        self.buttons = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

        self.label = Label(master, text=self.player + " turn", font=('consolas', 40))
        self.label.pack(side="top")

        self.reset_button = Button(master, text="Restart", font=('consolas', 20), command=self.new_game)
        self.reset_button.pack(side="top")

        self.frame = Frame(master)
        self.frame.pack()

        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(self.frame, text="", font=('consolas', 40), width=5, height=2,
                                                   command=lambda row=row, column=column: self.next_turn(row, column))
                self.buttons[row][column].grid(row=row, column=column)

    def next_turn(self, row, column):
        if self.buttons[row][column]['text'] == "" and self.check_winner() is False:
            if self.player == self.players[0]:
                self.buttons[row][column]['text'] = self.player
                if self.check_winner() is False:
                    self.player = self.players[1]
                    self.label.config(text=(self.players[1] + " turn"))
                elif self.check_winner() is True:
                    self.label.config(text=(self.players[0] + " won"))
                elif self.check_winner() == "draw":
                    self.label.config(text=("It's a draw!"))
            else:
                self.buttons[row][column]['text'] = self.player
                if self.check_winner() is False:
                    self.player = self.players[0]
                    self.label.config(text=(self.players[0] + " turn"))
                elif self.check_winner() is True:
                    self.label.config(text=(self.players[1] + " won"))
                elif self.check_winner() == "draw":
                    self.label.config(text=("It's a draw!"))

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                return True

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True

        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True

        elif self.empty_spaces() is False:
            return "draw"
        else:
            return False

    def empty_spaces(self):
        spaces = 9
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]['text'] != "":
                    spaces -= 1

        return spaces != 0

    def new_game(self):
        self.player = random.choice(self.players)
        self.label.config(text=self.player + " turn")

        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="")


if __name__ == "__main__":
    root = Tk()
    app = TicTacToe(root)
    root.mainloop()

