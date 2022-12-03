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

def strToMove(s: str) -> Move:
    if s in ['A']:
        return Move.ROCK
    elif s in ['B']:
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

def strToResult(s: str) -> Result:
    if s in ['X']:
        return Result.LOSS
    elif s in ['Y']:
        return Result.TIE
    else:
        return Result.WIN


def neededMove(opp: Move, desired: Result) -> Move:
    if opp == Move.ROCK and desired == Result.WIN:
        return Move.PAPER
    if opp == Move.ROCK and desired == Result.LOSS:
        return Move.SCISSORS
    if opp == Move.PAPER and desired == Result.WIN:
        return Move.SCISSORS
    if opp == Move.PAPER and desired == Result.LOSS:
        return Move.ROCK
    if opp == Move.SCISSORS and desired == Result.WIN:
        return Move.ROCK
    if opp == Move.SCISSORS and desired == Result.LOSS:
        return Move.PAPER
    else: 
        return opp

if __name__ == '__main__':
    total = 0

    for line in fileinput.input():
        opp, desired = line.strip().split(' ')
        oppMove = strToMove(opp)
        desiredResult = strToResult(desired)
        youMove = neededMove(oppMove, desiredResult)

        total += youMove.points() + desiredResult.points()

    print(total)