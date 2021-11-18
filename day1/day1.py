def part_one(expenses):
    for expense in expenses:
        for expense2 in expenses:
            if expense + expense2 == 2020:
                return expense * expense2

def part_two(expenses):
    for expense in expenses:
        for expense2 in expenses:
            for expense3 in expenses:
                if expense + expense2 + expense3 == 2020:
                    return expense * expense2 * expense3

if __name__ == 'main':
    expenses = []

    with open(r'C:\Users\ndepalma\Desktop\advent_2020\day1\input.txt') as f:
        for expense in f.readlines():
            expenses.append(int(expense.strip()))

    print(f'The answer to part one is {part_one(expenses)}')
    print(f'The answer to part two is {part_two(expenses)}')