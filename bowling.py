from dataclasses import dataclass
from random import randint
from typing import List


@dataclass
class Line:
    bowler: str
    tries: List[str]
    current_try: int = 0


def is_first_try(n: int) -> bool:
    return n % 2 == 0


def is_second_try(n: int) -> bool:
    return n % 2 != 0


def is_strike(result: str) -> bool:
    return result.isdigit() and int(result) >= 10


def is_spare(result1: str, result2: str) -> bool:
    return not is_strike(result1) and int(result1) + int(result2) >= 10


def add_try(line: Line, result: int) -> None:
    print(f'try nr. {line.current_try + 1} for bowler {line.bowler} thrown {result}')
    line.tries[line.current_try] = str(result)

    # check last frame (if strike or spare)
    if line.current_try > 1:
        if is_second_try(line.current_try):
            if is_strike(line.tries[line.current_try - 3]):
                line.tries[line.current_try - 3] = str(int(line.tries[line.current_try - 3]) + result)
        else:  # 1st try
            if is_strike(line.tries[line.current_try - 2]):
                line.tries[line.current_try - 2] = str(int(line.tries[line.current_try - 2]) + result)
                if line.current_try > 3 and is_strike(line.tries[line.current_try - 4]):  # double strike
                    line.tries[line.current_try - 4] = str(int(line.tries[line.current_try - 4]) + result)
            elif is_spare(line.tries[line.current_try - 1], line.tries[line.current_try - 2]):
                line.tries[line.current_try - 1] = str(int(line.tries[line.current_try - 1]) + result)


def skip_2nd_try_of_strike(line):
    line.tries[line.current_try] = 'X'


def skip_bonus_try(line):
    line.tries[line.current_try] = ''


def throw_or_skip(line: Line) -> None:
    if line.current_try < 22:
        if line.current_try == 20 and not is_strike(line.tries[18]) and not is_spare(line.tries[18], line.tries[19]):
            skip_bonus_try(line)  # no bonus try
        elif line.current_try == 21:
            if not is_strike(line.tries[18]):
                skip_bonus_try(line)  # no bonus try
            else:
                result = throw_first()
                add_try(line, result=result)
        elif is_first_try(line.current_try):
            result = throw_first()
            add_try(line, result=result)
        else:  # 2s try
            first_try_in_frame = line.tries[line.current_try - 1]
            if is_strike(first_try_in_frame):
                skip_2nd_try_of_strike(line)
            else:
                result = throw_second(int(first_try_in_frame))
                add_try(line, result=result)
        line.current_try += 1


def throw_second(first_throw: int):
    return randint(0, 10 - first_throw)


def throw_first():
    return randint(0, 10)


def total(line):
    result = 0
    for i in range(20):
        if line.tries[i].isdigit():
            result += int(line.tries[i])
    return result


def main() -> List[Line]:
    lines = [Line(bowler="Deyaa", tries=[''] * 22),
             Line(bowler="Andre", tries=[''] * 22),
             Line(bowler="Florian", tries=[''] * 22)]
    for try_nr in range(22):
        for bowler_nr in range(len(lines)):
            throw_or_skip(lines[bowler_nr])
        print('------------------')
    for line in lines:
        print(f'End result for {line.bowler} is {total(line)}: {line.tries}')
    return lines


if __name__ == '__main__':
    main()
