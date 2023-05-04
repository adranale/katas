from dataclasses import dataclass
from random import randint
from typing import List


@dataclass
class Line:
    bowler: str
    tries: List[int]
    current_try: int = 0


def first_try(n: int) -> bool:
    return n % 2 == 0  # even


def second_try(n: int) -> bool:
    return n % 2 != 0  # odd


def is_strike(result: int) -> bool:
    return result >= 10


def is_spare(result1: int, result2: int) -> bool:
    return not is_strike(result1) and result1 + result2 >= 10


def add_try(line: Line, result: int) -> None:
    print(f'try nr. {line.current_try + 1} for bowler {line.bowler} thrown {result}')
    line.tries[line.current_try] = result

    # check last frame (if strike or spare)
    # if line.current_try > 1:
    #     if is_second_try(line.current_try):  # 2nd try
    #         if is_strike(line.tries[line.current_try - 3]):
    #             line.tries[line.current_try - 3] += result
    #     else:  # 1st try
    #         if is_strike(line.tries[line.current_try - 2]):
    #             line.tries[line.current_try - 2] += result
    #         elif is_spare(line.tries[line.current_try - 1], line.tries[line.current_try - 2]):
    #             line.tries[line.current_try - 1] += result


def throw_or_skip(line: Line) -> None:
    if line.current_try < 22:
        if line.current_try == 20 and not is_spare(line.tries[18], line.tries[19]):
            pass  # no bonus try
        elif line.current_try == 21 and not is_strike(line.tries[18]):
            pass  # no bonus try
        elif first_try(line.current_try):  # 1s try in frame
            result = randint(0, 10)
            add_try(line, result=result)
        else:  # 2s try in frame
            first_try_in_frame = line.tries[line.current_try - 1]
            if is_strike(first_try_in_frame):
                pass  # skip next try
            else:
                result = randint(0, 10 - first_try_in_frame)
                add_try(line, result=result)
        line.current_try += 1


def add_bonus(line):
    for try_nr in range(20):
        if first_try(try_nr) and is_strike(line.tries[try_nr]):
            print(f'adding bonus for bowler {line.bowler} of {line.tries[try_nr+2]} for index {try_nr}: strike')
            line.tries[try_nr] += line.tries[try_nr + 2]
            if is_strike(line.tries[try_nr + 2]):
                print(f'adding bonus for bowler {line.bowler} of {line.tries[try_nr + 4]} for index {try_nr}: double strike')
                line.tries[try_nr] += line.tries[try_nr + 4]
            else:
                print(f'adding bonus for bowler {line.bowler} of {line.tries[try_nr + 3]} for index {try_nr}: single strike')
                line.tries[try_nr] += line.tries[try_nr + 3]
        elif second_try(try_nr) and is_spare(line.tries[try_nr - 1], line.tries[try_nr]):
            print(f'adding bonus for bowler {line.bowler} of {line.tries[try_nr+1]} for index {try_nr}: spare')
            line.tries[try_nr] += line.tries[try_nr+1]


def add_bonus_wrong(line):
    for try_nr in range(21, 2, -1):
        if second_try(line.tries[try_nr]):  # 2nd try
            if is_strike(line.tries[try_nr - 3]):
                print(f'adding bonus for bowler {line.bowler} of {line.tries[try_nr]} for index {try_nr - 3}: line.tries[try_nr - 3] += line.tries[try_nr]')
                line.tries[try_nr - 3] += line.tries[try_nr]
        else:  # 1st try
            if is_strike(line.tries[try_nr - 2]):
                print(f'adding bonus for bowler {line.bowler} of {line.tries[try_nr]} for index {try_nr - 2}: line.tries[try_nr - 2] += line.tries[try_nr]')
                line.tries[try_nr - 2] += line.tries[try_nr]
            elif is_spare(line.tries[try_nr - 1], line.tries[try_nr - 2]):
                print(f'adding bonus for bowler {line.bowler} of {line.tries[try_nr]} for index {try_nr - 1}: line.tries[try_nr - 1] += line.tries[try_nr]')
                line.tries[try_nr - 1] += line.tries[try_nr]


if __name__ == '__main__':
    lines = [Line(bowler="Deyaa", tries=[0] * 22),
             Line(bowler="Andre", tries=[0] * 22),
             Line(bowler="Florian", tries=[0] * 22)]

    for try_nr in range(22):
        for bowler_nr in range(len(lines)):
            throw_or_skip(lines[bowler_nr])
        print('------------------')

    index_array = [i for i in range(22)]
    # print(f'{index_array} is index')

    for line in lines:
        print(f'{line.tries}. Result before bonus for {line.bowler} is {sum(line.tries)}')

    print('------------------')

    # print(f'{index_array} is index')
    for line in lines:
        add_bonus(line)

    print('------------------')

    # print(f'{index_array} is index')
    for line in lines:
        print(f'{line.tries}. End result for {line.bowler} is {sum(line.tries)}')
