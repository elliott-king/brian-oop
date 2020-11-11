# The prime goal in writing code is making it readable & easily understandable. 
# Object Oriented Programming simply helps with that.

WIN_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

class Board:
    def __init__(self, board=[" "]*9):
        self.board = board

    def display(self):
        print(" " + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("-----------")
        print(" " + self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("-----------")
        print(" " + self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def valid_move(self, index):
        # TODO: should return True if valid, False if not
        if self.board[index] == " ":
            return True
        return False

    def move(self, index, token):
        # TODO: does not need to return anything, but should update the board
        self.board[index] = token

    def check_combination(self, combination):
        if self.board[combination[0]] == self.board[combination[1]] and self.board[combination[1]] == self.board[combination[2]] and self.board[combination[0]] != " ":
            return True
        return False
        # TODO: check if all spots in a combination are taken by the same player. Return T or F
        

    def is_full(self):
        # TODO: check if board is full, return T/F
        if " " in self.board:
            return False
        return True

    def is_won(self):
        for combination in WIN_COMBINATIONS:
            if self.check_combination(combination):
                return True
        return False

    # A bit of duplicated code, but whatever.
    def winning_token(self):
        for combination in WIN_COMBINATIONS:
            if self.check_combination(combination):
                # All squares in the winning combo should have the same value, we can take the first
                return self.board[combination[0]]

    def is_draw(self):
        return self.is_full() and not self.is_won()

class Game:
    # The init fn holds all setup logic. 
    def __init__(self):
        self.game_board = Board()
        self.player1 = "" # this is just a placeholder
        self.player2 = "" 
        self.current_token = "X"

    # Humans read tic-tac-toe spaces as 1-9, but a computer starts at 0.
    def input_to_index(self, user_input):
        return int(user_input) - 1

    # helper method to get player name from current token
    def current_player(self):
        # TODO: return name of current player
        if self.current_token =="X":
            return self.player1
        else:
            return self.player2

    def update_token(self):
        # TODO: cycle the current token
        if self.current_token == "X":
            self.current_token = "O"
        else:
            self.current_token = "X"

    def turn(self):
        user_input = 10
        while user_input > 9:
            user_input = int(input(str(self.current_player()) + ", please enter a space to choose (1-9):"))
        index = self.input_to_index(user_input)
        if self.game_board.valid_move(index):
            self.game_board.move(index, self.current_token)
            self.game_board.display()
            self.update_token()
        else:
            print("That was not a valid move")

    # This just returns the combination of two conditionals.
    def game_over(self):
        return self.game_board.is_won() or self.game_board.is_draw()

    def get_player_names(self):
        self.player1 = input("What is the name of player 1? ")
        self.player2 = input("What is the name of player 2? ")
        print("Now playing with players", self.player1, "and", self.player2)

    def winner(self):
        if self.game_board.winning_token() == "X":
            return self.player1
        else:
            return self.player2
        pass

    # This fn controls the flow of the game
    def turn_cycle(self):
        # First, we get the player names
        self.get_player_names()
        # Second, play turns until the game is over
        while not self.game_over():
            self.turn()
        # Finally, declare a winner
        if self.game_board.is_won():
            winner = self.winner()
            print("Congratulations, ", winner)
        else:
            print("Tie game!")

# This code will run a game if you run the script by `python3 tictactoe.py`
if __name__ == "__main__":
    g = Game()
    g.turn_cycle()