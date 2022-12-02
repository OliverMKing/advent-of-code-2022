import fileinput
from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3 

    def points(self) -> int:
        if self == Move.ROCK:
            return 1
        if self == Move.PAPER:
            return 2
        else:
            return 3

def letterToMove(letter: str) -> Move:
    if letter in ['A', 'X']:
        return Move.ROCK
    elif letter in ['B', 'Y']:
        return Move.PAPER
    else:
        return Move.SCISSORS

class Result(Enum):
    LOSS = 1
    TIE = 2
    WIN = 3

    def points(self) -> int:
        if self == Result.LOSS:
            return 0
        elif self == Result.TIE:
            return 3
        else:
            return 6

def movesToResult(opp: Move, you: Move) -> Result:
    if opp == Move.ROCK and you == Move.PAPER:
        return Result.WIN
    elif opp == Move.ROCK and you == Move.SCISSORS:
        return Result.LOSS
    elif opp == Move.PAPER and you == Move.ROCK:
        return Result.LOSS
    elif opp == Move.PAPER and you == Move.SCISSORS:
        return Result.WIN
    elif opp == Move.SCISSORS and you == Move.ROCK:
        return Result.WIN
    elif opp == Move.SCISSORS and you == Move.PAPER:
        return Result.LOSS
    else:
        return Result.TIE

if __name__ == '__main__':
    total = 0

    for line in fileinput.input():
        opp, you = line.strip().split(' ')
        oppMove, youMove = map(letterToMove, (opp, you))
        result = movesToResult(oppMove, youMove)

        total += youMove.points() + result.points()

    print(total)