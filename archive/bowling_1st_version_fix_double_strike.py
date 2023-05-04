from dataclasses import dataclass
from random import randint
from typing import List


@dataclass
class Line:
    bowler: str
    tries: List[int]
    current_try: int = 0


def first_try(n: int) -> bool:
    return n % 2 == 0


def second_try(n: int) -> bool:
    return n % 2 != 0


def is_strike(result: int) -> bool:
    return result >= 10


def is_spare(result1: int, result2: int) -> bool:
    return not is_strike(result1) and result1 + result2 >= 10


def add_try(line: Line, result: int) -> None:
    print(f'try nr. {line.current_try + 1} for bowler {line.bowler} thrown {result}')
    line.tries[line.current_try] = result

    # check last frame (if strike or spare)
    if line.current_try > 1:
        if second_try(line.current_try):
            if is_strike(line.tries[line.current_try - 3]):
                line.tries[line.current_try - 3] += result
        else:  # 1st try
            if is_strike(line.tries[line.current_try - 2]):
                line.tries[line.current_try - 2] += result
                if line.current_try > 3 and is_strike(line.tries[line.current_try - 4]):  # double strike
                    line.tries[line.current_try - 4] += result
            elif is_spare(line.tries[line.current_try - 1], line.tries[line.current_try - 2]):
                line.tries[line.current_try - 1] += result


def skip_try(line):
    line.tries[line.current_try] = -1


def throw_or_skip(line: Line) -> None:
    if line.current_try < 22:
        if line.current_try == 20 and not is_spare(line.tries[18], line.tries[19]):
            skip_try(line)  # no bonus try
        elif line.current_try == 21 and not is_strike(line.tries[18]):
            skip_try(line)  # no bonus try
        elif first_try(line.current_try):
            result = randint(0, 10)
            add_try(line, result=result)
        else:  # 2s try
            first_try_in_frame = line.tries[line.current_try - 1]
            if is_strike(first_try_in_frame):
                skip_try(line)
            else:
                result = randint(0, 10 - first_try_in_frame)
                add_try(line, result=result)
        line.current_try += 1


if __name__ == '__main__':
    lines = [Line(bowler="Deyaa", tries=[0] * 22),
             Line(bowler="Andre", tries=[0] * 22),
             Line(bowler="Florian", tries=[0] * 22)]
    for try_nr in range(22):
        for bowler_nr in range(len(lines)):
            throw_or_skip(lines[bowler_nr])
        print('------------------')

    for line in lines:
        print(f'End result for {line.bowler} is {sum(line.tries)}: {line.tries}')
