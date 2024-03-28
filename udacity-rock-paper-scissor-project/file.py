import random
import time


def print_pause(message):
    print(message)
    time.sleep(1)


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def choose_move(self):
        while True:
            move = input("Choose: rock, paper, or scissors? ").lower()
            if move in ['rock', 'paper', 'scissors']:
                return move
            else:
                print_pause("Invalid move. "
                            "Please choose "
                            "'rock', 'paper', or 'scissors'.")


class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors'])


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = None

    def move(self):
        if self.last_move is None:
            return random.choice(['rock', 'paper', 'scissors'])
        return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.cycle_moves = ['rock', 'paper', 'scissors']
        self.index = 0

    def move(self):
        move = self.cycle_moves[self.index]
        self.index = (self.index + 1) % len(self.cycle_moves)
        return move

    def learn(self, my_move, their_move):
        self.last_move = their_move


class AllRockerPlayer(Player):
    def move(self):
        return 'rock'


class HumanPlayer(Player):
    pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.choose_move()
        move2 = self.p2.move()
        print_pause(f"You: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print_pause("You win!")
        elif beats(move2, move1):
            self.p2_score += 1
            print_pause("Player 2 wins!")
        else:
            print_pause("It's a tie!")
        if hasattr(self.p1, 'learn'):
            self.p1.learn(move1, move2)
        if hasattr(self.p2, 'learn'):
            self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("Welcome to Rock, Paper, Scissors!")
        print_pause("This is a best of 3 match")
        print_pause("Good Luck")
        while self.p1_score < 2 and self.p2_score < 2:
            self.play_round()
            print_pause(f"Score:You- {self.p1_score} Player2- {self.p2_score}")
            print_pause("")

        if self.p1_score > self.p2_score:
            print_pause("You win the game!")
        else:
            print_pause("Player 2 wins the game!")
        print_pause("Game over!")
        self.play_again()

    def play_again(self):
        while True:
            play_again = input("Play again? (yes/no): ").lower()
            if play_again == 'yes':
                new_game = Game(Player(), RandomPlayer())
                new_game.play_game()
                return
            elif play_again == 'no':
                print_pause("Thanks for playing!")
                quit()
            else:
                print_pause("Invalid input. "
                            "Please enter 'yes' or 'no'.")


if __name__ == '__main__':
    game = Game(Player(), RandomPlayer())
    game.play_game()

random_player = RandomPlayer()
print(random_player.move())

reflect_player = ReflectPlayer()
print(reflect_player.move())

cycle_player = CyclePlayer()
print(cycle_player.move())

all_rocker_player = AllRockerPlayer()
print(all_rocker_player.move())

human_player = HumanPlayer()
print(human_player.move())
