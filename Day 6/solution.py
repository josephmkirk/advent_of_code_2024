# SOLUTION FOR ADVENT OF CODE 2024 DAY 6

# Link https://adventofcode.com/2024/day/6

import copy

class guard():
    # Initalise
    def __init__(self, map):
        self.reset(map)

    # Reset direction and position to start/north
    def reset(self, map):
        self.position = find_start_point(map)
        self.direction = 0

    # Get new position to consider based on direction
    def get_new_pos(self):
        # North
        if self.direction == 0:
            step = [-1,0]
        # East
        elif self.direction == 1:
            step = [0,1]
        # South
        elif self.direction == 2:
            step = [1,0]
        # West
        elif self.direction == 3:
            step = [0,-1]
            
        new_position = [self.position[0] + step[0], self.position[1] + step[1]]
        return new_position

    # Simulate patrol
    def patrol(self, map): 
        # Part 2
        # Object with (x,y): [directions] as key:value
        obstacle_collisions = {}

        # Until exit (or loop discovered)
        while True:
            # Set as visited
            map[self.position[0]][self.position[1]] = "X"

            # Get next step
            new_position = self.get_new_pos()

            # Check out of bounds, if so success
            if (new_position[0] >= len(map) or
                new_position[0] < 0 or
                new_position[1] >= len(map[0]) or
                new_position[1] < 0):
                return map, 0
            
            # Check if hit obstacle
            elif map[new_position[0]][new_position[1]] == "#":
                coords = (new_position[0], new_position[1])

                # If already collided before, i.e. entry exists
                if coords in obstacle_collisions.keys():

                    # If already collided from that direction, loop exists
                    if self.direction in obstacle_collisions[coords]:
                        return map, 1
                    
                    # Else add collision from current direction
                    else:
                        obstacle_collisions[coords].append(self.direction)
                
                # Else create entry
                else:
                    obstacle_collisions[coords] = [self.direction]

                # Turn right
                self.direction = (self.direction + 1) % 4        

            else:
                #Move
                self.position = new_position


# Utility functions

# Prints map nicely
def print_map(map):
    print("_______________")
    for line in map:
        print("".join(line))

def find_start_point(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                return (i,j)

# Part 1
def part1(map):
    # Create guard
    guard1 = guard(map)

    # Copy map and simulate patrol
    patrolled_map, _ = guard1.patrol(copy.deepcopy(map))
    print_map(patrolled_map)

    # Count number of Xs
    total = 0
    for line in patrolled_map:
        for point in line:
            if point == "X":
                total += 1

    return total

# Part 2
def part2(map):
    # Run simulation once
    guard1 = guard(map)
    patrolled_map, _ = guard1.patrol(copy.deepcopy(map))

    total = 0
    # Collect points where single obstacle could be placed to detour guard
    # Loop through all visited places

    for i in range(len(patrolled_map)):
        print(i)
        for j in range(len(patrolled_map[1])):

            # If visited
            if patrolled_map[i][j] == "X":
                # Create copy and add new obstacles
                copy_map = copy.deepcopy(map)
                copy_map[i][j] = "#"

                # Reset guard
                guard1.reset(map)
                
                # Simulate patrol
                test, loop_found = guard1.patrol(copy_map)

                if test:
                    total += loop_found

    return total

map = []

# File handling
file = open("input.txt", "r")

for line in file.readlines():
    map.append(list(line.strip("\n")))


print(f"Part 1: {part1(map)}")
print(f"Part 2: {part2(map)}")
