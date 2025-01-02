# SOLUTION FOR ADVENT OF CODE 2024 DAY 8

# Link https://adventofcode.com/2024/day/8

from itertools import combinations
import copy

# Prints map nicely formatted for debugging
def print_map(city_map):
    for line in city_map:
        print("".join(line))


# Find all occurences of any signal and store as key: [coords] pairs
def get_antennas(city_map):
    antennas = {}

    for i in range(len(city_map)):
        for j, symbol in enumerate(city_map[i]):

            if not symbol == ".":
                if symbol in antennas.keys():
                    antennas[symbol].append([i,j])

                else:
                    antennas[symbol] = [[i,j]]

    return antennas

def part1(city_map):
    # Get antennas
    antennas = get_antennas(city_map)

    # Generate blank map of same size to record nodes
    blank_map = [["." for i in city_map[0]] for j in city_map]

    # Loop through all unique signals
    for key in antennas.keys():

        # Check at least 2 antennas exist
        if len(antennas[key]) > 1:

            # Get all combinations of pairs of antennas
            pairs = list(combinations(antennas[key], 2))

            # Loop through
            for pair in pairs:

                # Find displacement as [x,y] vector
                difference = (pair[1][0]-pair[0][0], pair[1][1]-pair[0][1])
                
                # If moving along line created by antennas is in bounds, mark
                if (0 <= pair[0][0] - difference[0] < len(city_map) and
                    0 <= pair[0][1] - difference[1] < len(city_map)):
                    blank_map[pair[0][0] - difference[0]][pair[0][1] - difference[1]] = "#"

                # Same for other direction
                if (0 <= pair[1][0] + difference[0] < len(city_map) and
                    0 <= pair[1][1] + difference[1] < len(city_map)):
                    blank_map[pair[1][0] + difference[0]][pair[1][1] + difference[1]] = "#"

    # Count all marked spots in blank map
    count = 0
    for i in blank_map:
        for j in i:
            if j == "#":
                count += 1

    return count


def part2(city_map):
    # Get antennas
    antennas = get_antennas(city_map)

    # Generate blank map of same size to record nodes
    blank_map = [["." for i in city_map[0]] for j in city_map]

    # Loop through all unique signals
    for key in antennas.keys():

        # Check at least 2 antennas exist
        if len(antennas[key]) > 1:
            pairs = list(combinations(antennas[key], 2))
            
            # Get all combinations of pairs of antennas
            for pair in pairs:

                # Find displacement as [x,y] vector
                difference = (pair[1][0]-pair[0][0], pair[1][1]-pair[0][1])

                # Same as in part 1, but this time marking all points at the fixed interval until out of bounds
                # Create copy to track offset
                current_pos = copy.copy(pair[0])
                # Mark antenna as antinode as well
                blank_map[current_pos[0]][current_pos[1]] = "#"

                # Check not out of bound
                while (0 <= current_pos[0] - difference[0] < len(city_map) and
                       0 <= current_pos[1] - difference[1] < len(city_map)):
                    
                    # Offset
                    current_pos[0] -= difference[0]
                    current_pos[1] -= difference[1]

                    # Mark
                    blank_map[current_pos[0]][current_pos[1]] = "#"

                # Repeat for other direction
                current_pos = copy.copy(pair[1])
                blank_map[current_pos[0]][current_pos[1]] = "#"

                while (0 <= current_pos[0] + difference[0] < len(city_map) and
                       0 <= current_pos[1] + difference[1] < len(city_map)):
                    
                    current_pos[0] += difference[0]
                    current_pos[1] += difference[1]

                    blank_map[current_pos[0]][current_pos[1]] = "#"

    # Count all marked spots in blank map
    count = 0
    for i in blank_map:
        for j in i:
            if j == "#":
                count += 1

    return count



# Input formatting / 2D array generation
file = open("input.txt", "r")

city_map = []
for line in file.readlines():
    city_map.append(list(line.strip("\n")))


print(f"Part 1: {part1(city_map)}")
print(f"Part 2: {part2(city_map)}")