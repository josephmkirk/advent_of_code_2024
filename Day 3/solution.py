# SOLUTION FOR ADVENT OF CODE 2024 DAY 3

# Link https://adventofcode.com/2024/day/3

import re

# Part 1
def part1(file):
    # Regex expression
    regex = r"mul\((\d+),(\d+)\)"

    # Find all matches
    matches = re.findall(regex, file)

    # Extracting two separate lists for a and b
    a_list = [int(a) for a, b in matches]
    b_list = [int(b) for a, b in matches]

    # Pair up and multiply
    result = [a * b for a, b in zip(a_list, b_list)]

    # Return sum
    return sum(result)

# Part 2
def part2(file):
    # Split up into "do()" occurrences
    do_split = file.split("do()")
    
    total = 0
    for s in do_split:
        # Split up into don'ts
        dont_split = s.split("don't()")

        # Every "mul(x,y)" before the first "dont'()" will be valid
        total += part1(dont_split[0])        

    return total

# Filehandling
file = open("input.txt", "r").readline()

print(part1(file))
print(part2(file))



