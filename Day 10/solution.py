# SOLUTION FOR ADVENT OF CODE 2024 DAY 10

# Link https://adventofcode.com/2024/day/10

class hiker():
    def __init__(self, map):
        self.map = map

        # Part 2
        self.ratings = {}

    # Essentially dfs
    def search_trails(self, x, y, trailheads, startpoint):
        # Base case
        # Is current position a 9
        if self.map[y][x] == 9:

            # Part 2
            if startpoint in self.ratings:
                self.ratings[startpoint] += 1
            else:
                self.ratings[startpoint] = 1

            # Uses set to ensure each trail only found once
            return set([(x, y)])

        # Recursive
        # 4 different directions
        # All edge checked 
        
        if 0 < y:
            # North/Up
            if self.map[y-1][x] - self.map[y][x] == 1:
                set.update(trailheads, self.search_trails(x, y-1, trailheads, startpoint))
        
        if y < len(self.map)-1:
            # South/Down
            if self.map[y+1][x] - self.map[y][x] == 1:
                set.update(trailheads, self.search_trails(x, y+1, trailheads, startpoint))

        if 0 < x:
            # West/Left
            if self.map[y][x-1] - self.map[y][x] == 1:
                set.update(trailheads, self.search_trails(x-1, y, trailheads, startpoint))

        if x < len(self.map[0])-1:
            # East/Right
            if self.map[y][x+1] - self.map[y][x] == 1:
                set.update(trailheads, self.search_trails(x+1, y, trailheads, startpoint))

        return trailheads

 
# Filehandling
file = open("input.txt", "r")

topo_map = []
starting_positions = []

# Generate map
for line in file.readlines():
    line = list(line.strip("\n"))
    topo_map.append([int(i) for i in line])

# Initalise
dave = hiker(topo_map)

# Loop through all starting points and search
trails = {}
for y in range(len(topo_map)):
    for x in range(len(topo_map[y])):
        if topo_map[y][x] == 0:

            trails[(x,y)] = dave.search_trails(x, y, set(), (x,y))

# Sum up scores
scores = 0
for key in trails.keys():
    scores += len(trails[key])

print(f"Part 1: {scores}")

# Sum up ratings
ratings = 0
for key in dave.ratings.keys():
    ratings += dave.ratings[key]

print(f"Part 2: {ratings}")

