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


def differ_by_exactly_1_letter(word1, word2):
    one_difference_found = False

    for i, letter in enumerate(word1):
        if word2[i] != letter:
            if one_difference_found:
                return False
            one_difference_found = True

    return one_difference_found


def find_common_letters(word1, word2):
    def yield_letters():
        for i, letter in enumerate(word1):
            if word2[i] == letter:
                yield letter
    return "".join(list(yield_letters()))


def solve_puzzle_2(puzzle_input):
    words = list(filter(lambda line: line != "", puzzle_input.split("\n")))
    found = False
    for word1 in words:
        for word2 in words:
            if differ_by_exactly_1_letter(word1, word2):
                found = True
                print("Answer for day1, exercise 2: %s" % find_common_letters(word1, word2))
                break
        if found:
            break


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No input_exercise1 given. Specify a path to the input_exercise1 file.")
        print("python main.py path-to-input_exercise1")
    else:
        solve_puzzle_1(open(sys.argv[1]).read())
        solve_puzzle_2(open(sys.argv[1]).read())
