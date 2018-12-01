import sys
from collections import defaultdict


def count_sum_of_lines_with_numbers(lines_with_numbers):
    return sum(map(int, lines_with_numbers))


def solve_puzzle_1(puzzle_input):
    lines_with_numbers = filter(lambda line: line != "", puzzle_input.split("\n"))
    print("Answer for day1, exercise 1: %s" % count_sum_of_lines_with_numbers(lines_with_numbers))


def solve_puzzle_2(puzzle_input):
    lines_with_numbers = filter(lambda line: line != "", puzzle_input.split("\n"))
    numbers = list(map(int, lines_with_numbers))

    frequencies_occurrence = defaultdict(int)
    current_frequency = 0
    frequencies_occurrence[current_frequency] += 1

    numbers_count = len(numbers)
    i = 0
    while True:
        number = numbers[i % numbers_count]
        current_frequency += number
        frequencies_occurrence[current_frequency] += 1
        if frequencies_occurrence[current_frequency] == 2:
            print("Answer for day1, exercise 2: %s" % current_frequency)
            break
        i += 1


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No input given. Specify a path to the input file.")
        print("python main.py path-to-input")
    else:
        solve_puzzle_1(open(sys.argv[1]).read())
        solve_puzzle_2(open(sys.argv[1]).read())
