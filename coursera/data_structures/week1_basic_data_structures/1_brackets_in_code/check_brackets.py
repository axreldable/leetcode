# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0 or not are_matching(opening_brackets_stack.pop()[0], next):
                return i + 1

    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0][1]
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()

    # files = listdir("tests")
    # files.sort()
    # for i, file in enumerate(files):
    #     if file.endswith(".a"):
    #         task = open("tests/" + files[i - 1], "r").read().strip()
    #         answer = open("tests/" + files[i], "r").read().strip()
    #         rez = find_mismatch(task)
    #         # print(task, answer, rez)
    #         assert str(rez) == str(answer)
