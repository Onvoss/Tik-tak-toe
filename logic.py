import random

class TicTacToeLogic:
    def __init__(self):
        self.players = ["X", "O"]
        self.player = random.choice(self.players)
        self.buttons = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def next_turn(self, row, column):
        if self.buttons[row][column] == "" and not self.check_winner():
            self.buttons[row][column] = self.player
            if not self.check_winner():
                self.player = self.players[1] if self.player == self.players[0] else self.players[0]

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0] == self.buttons[row][1] == self.buttons[row][2] != "":
                return True

        for column in range(3):
            if self.buttons[0][column] == self.buttons[1][column] == self.buttons[2][column] != "":
                return True

        if self.buttons[0][0] == self.buttons[1][1] == self.buttons[2][2] != "":
            return True

        elif self.buttons[0][2] == self.buttons[1][1] == self.buttons[2][0] != "":
            return True

        elif not self.empty_spaces():
            return "döntetlen"

        else:
            return False

    def empty_spaces(self):
        spaces = 9
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column] != "":
                    spaces -= 1
        return spaces != 0