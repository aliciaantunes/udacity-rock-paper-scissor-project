import random
import time


def print_pause(message):
    print(message)
    time.sleep(1)


class Player:
    def __init__(self):
        self.last_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Choose rock, paper, or scissors: ").lower()
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            else:
                print_pause("Invalid choice. Please choose again.")


class RockerPlayer(Player):
    pass  # Inherits move method from Player, always returns 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors'])


class MimicPlayer(Player):
    def move(self):
        if self.last_move is None:
            return random.choice(['rock', 'paper', 'scissors'])
        return self.last_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.moves = ['rock', 'paper', 'scissors']
        self.index = 0

    def move(self):
        choice = self.moves[self.index]
        self.index = (self.index + 1) % len(self.moves)
        return choice


BEATS = {'rock': 'scissors',
         'scissors': 'paper',
         'paper': 'rock'}


def beats(one, two):
    return BEATS[one] == two


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scores = {self.p1: 0, self.p2: 0}

    def show_scores(self):
        print_pause("Current Scores:")
        print_pause(f"Player 1: {self.scores[self.p1]}")
        print_pause(f"Player 2: {self.scores[self.p2]}")

    def play_round(self):
        move1, move2 = self.p1.move(), self.p2.move()
        print_pause(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print_pause("It's a tie!")
        elif beats(move1, move2):
            self.scores[self.p1] += 1
            print_pause("Player 1 wins!")
        else:
            self.scores[self.p2] += 1
            print_pause("Player 2 wins!")

        self.show_scores()  # Chama a função para mostrar o placar
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("Game start!")
        round_number = 1
        while self.scores[self.p1] < 3 and self.scores[self.p2] < 3:
            print_pause(f"Round {round_number}:")
            self.play_round()
            round_number += 1
        if self.scores[self.p1] > self.scores[self.p2]:
            print_pause("Player 1 wins the game!")
        else:
            print_pause("Player 2 wins the game!")
        print_pause("Game over!")


def select_random_computer_player():
    computer_player_types = [RockerPlayer, RandomPlayer,
                             MimicPlayer, CyclePlayer]
    selected_type = random.choice(computer_player_types)
    return selected_type()


if __name__ == '__main__':
    while True:
        computer_player = select_random_computer_player()
        game = Game(HumanPlayer(), computer_player)
        game.play_game()

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            break
