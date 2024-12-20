# SOLUTION FOR ADVENT OF CODE 2024 DAY 4

# Link https://adventofcode.com/2024/day/4

# Searching ----
def search_WE(board, keyword):
    total = 0

    # Loop over board
    for i in range(len(board)):
        for j in range(len(board[0]) - len(keyword)+1):

            # Define section
            section = board[i][j:j+4]

            # Check against keyword and keyword reversed
            if section == keyword or section == keyword[::-1]:
                total += 1
    
    return total

# Searching |
def search_NS(board, keyword):
    total = 0

    # Loop over board
    for i in range(len(board) - len(keyword)+1):
        for j in range(len(board[0])):

            # Define section
            section = [board[i+x][j] for x in range(len(keyword))]
            
            # Check against keyword and keyword reversed
            if section == keyword or section == keyword[::-1]:
                total += 1

    return total

# Searching /
def search_NE(board, keyword):
    # Part 2
    coords = []

    # Loop over board
    for i in range(len(keyword)-1, len(board)):
        for j in range(len(board[0]) - len(keyword)+1):

            # Define section
            section = [board[i-x][j+x] for x in range(len(keyword))]
            
            # # Check against keyword and keyword reversed
            if section == keyword or section == keyword[::-1]:
                # Adapted for part 2
                coords.append((i-1, j+1))

    return coords

# Searching \
def search_SE(board, keyword):
    # Part 2
    coords = []

    # Loop over board
    for i in range(len(board) - len(keyword)+1):
        for j in range(len(board[0]) - len(keyword)+1):

            # Define section
            section = [board[i+x][j+x] for x in range(len(keyword))]
            
            # # Check against keyword and keyword reversed
            if section == keyword or section == keyword[::-1]:
                # Adapted for part 2
                coords.append((i+1, j+1))

    return coords

def part1(board, keyword):
    return (search_WE(board,keyword) + 
            search_NS(board,keyword) +
            len(search_NE(board,keyword)) +
            len(search_SE(board,keyword)))

def part2(board, keyword):
    coords1 = search_NE(board,keyword)
    coords2 = search_SE(board,keyword)

    total = 0
    for c in coords1:
        if c in coords2:
            total += 1

    return total

# Filehandling
file = open("input.txt", "r")

board = []
for line in file.readlines():
    board.append(list(line.strip("\n")))


print(part1(board,list("XMAS")))
print(part2(board,list("MAS")))

