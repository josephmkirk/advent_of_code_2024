# SOLUTION FOR ADVENT OF CODE 2024 DAY 1

# Link https://adventofcode.com/2024/day/1

import math

def merge_sort(input):

    # Get size
    size = len(input)

    # Recursive case
    # If larger than 2, half and then sort
    if size > 2:
        list1 = merge_sort(input[:size//2])
        list2 = merge_sort(input[size//2:])

        # Combine sorted lists
        output_list = []
        for i in range(size):
            if len(list1) == 0:
                output_list += list2
                break
            elif len(list2) == 0:
                output_list += list1
                break
            elif list1[0] < list2[0]:
                output_list.append(list1.pop(0))
            else:
                output_list.append(list2.pop(0))

        return output_list

    # Base case 1, edge case
    elif len(input) == 1:
        return input

    # Base case 2, if only 2 values then sort
    else:
        if input[0] < input[1]:
            return input
        else:
            return [input[1], input[0]]


def part1(list1, list2):
    # Sort lists
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)

    # Find overall difference
    total = 0
    for i in range(len(list1)):
        total += math.fabs(list1[i] - list2[i])

    return int(total)

def part2(list1, list2):    
    # Convert to set for unique values
    list1 = set(list1)

    # Find similarity score
    total = 0
    for i in list1:
        total += i * list2.count(i)

    return total

# Input file handling
file = open("input.txt", "r")

list1 = []
list2 = []

for line in file.readlines():
    line = line.strip("\n").split("   ")
    list1.append(int(line[0]))
    list2.append(int(line[1]))

print(part1(list1,list2))
print(part2(list1,list2))

