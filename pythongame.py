import random

class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = None
        self.their_move = None
        self.score = 0

    def validate_move(self, move):
        return move.lower() in self.moves

    def learn(self, my_move, their_move):
        pass

    def remember(self):
        pass


class HumanPlayer(Player):
    behavior = 'Human Player'

    def move(self):
        while True:
            move = input(
                'CHOOSE A MOVE: (rock / paper / scissors)\n').lower()
            if self.validate_move(move):
                return move
            else:
                print('Invalid move. Try again!')


class RandomPlayer(Player):
    behavior = 'Random Player'

    def move(self):
        return self.their_move or random.choice(self.moves)

    def learn(self, my_move, their_move):
        pass

    def remember(self):
        pass


class RepeatPlayer(Player):
    behavior = 'Repeat Player'

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def remember(self):
        pass


class ReflectPlayer(Player):
    behavior = 'Reflect Player'

    def move(self):
        return self.their_move or random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def remember(self):
        pass


class CyclePlayer(Player):
    behavior = 'Cycle Player'
    move_index = 0

    def move(self):
        m = self.moves[self.move_index]
        self.move_index = (self.move_index + 1) % len(self.moves)
        return m

    def learn(self, my_move, their_move):
        pass

    def remember(self):
        pass


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()

        print(f'Player 1: {move1}  Player 2: {move2}')

        if self.play1_wins(move1, move2):
            self.player1.score += 1
            print('-- YOU WIN! --\n')
        elif self.play2_wins(move1, move2):
            self.player2.score += 1
            print('-- COMPUTER WINS! --\n')
        else:
            print("-- IT'S A TIE --\n")

        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)
        self.player1.remember()
        self.player2.remember()
        print('       SCORE')
        print(
            f'Human: {self.player1.score} | {self.player2.behavior}: {self.player2.score}\n'
        )

    def play_game(self, rounds=3):
        print('Game starts!\n')
        for _ in range(rounds):
            print('Round:')
            self.play_round()
        print('Game over!\n\n')
        print('FINAL SCORE:')
        print(
            f'Human: {self.player1.score} | {self.player2.behavior}: {self.player2.score}'
        )

        self.player1.score = 0
        self.player2.score = 0

    def play1_wins(self, one, two):
        return (
            (one == 'scissors' and two == 'paper')
            or (one == 'paper' and two == 'rock')
            or (one == 'rock' and two == 'scissors')
        )

    def play2_wins(self, one, two):
        return (
            (one == 'paper' and two == 'scissors')
            or (one == 'rock' and two == 'paper')
            or (one == 'scissors' and two == 'rock')
        )


def start_new_game():
    behaviors = {
        'human': HumanPlayer(),
        'random': RandomPlayer(),
        'repeat': RepeatPlayer(),
        'reflect': ReflectPlayer(),
        'cycle': CyclePlayer(),
    }

    while True:
        print('ROCK, PAPER, SCISSORS - GO!\n')

        choice = input(
            'CHOOSE AN OPPONENT: (random / repeat / reflect / cycle / exit)\n'
        ).lower()

        if choice == 'exit':
            break
        elif choice in behaviors:
            game = Game(HumanPlayer(), behaviors[choice])
            game.play_game()
        else:
            print('Invalid choice. Try again!')


if __name__ == '__main__':
    start_new_game()
