import sys
from collections import defaultdict


def solve_puzzle_1(puzzle_input):
    words = filter(lambda line: line != "", puzzle_input.split("\n"))
    count_exactly_2 = 0
    count_exactly_3 = 0

    for word in words:
        letters_counter = defaultdict(int)

        for letter in word:
            letters_counter[letter] += 1

        found_2 = False
        found_3 = False

        for letter_count in letters_counter.values():
            found_2 = found_2 or letter_count == 2
            found_3 = found_3 or letter_count == 3
            if found_2 and found_3:
                break

        count_exactly_2 += 1 and found_2
        count_exactly_3 += 1 and found_3

    checksum = count_exactly_2 * count_exactly_3
    print("Answer for day1, exercise 1: %s" % checksum)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No input given. Specify a path to the input file.")
        print("python main.py path-to-input")
    else:
        solve_puzzle_1(open(sys.argv[1]).read())
