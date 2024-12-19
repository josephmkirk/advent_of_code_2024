# SOLUTION FOR ADVENT OF CODE 2024 DAY 2

# Link https://adventofcode.com/2024/day/2

# PART 1

def analyse_part1(report):
    # For sign check
    total = 0

    # Calc difference
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]

        # Check if jump level is unsafe
        if abs(diff) < 1 or abs(diff) > 3:
            return 0
        
        # Check if polarity is inconsistent
        total += diff / abs(diff)
        if abs(total) != i+1:
            return 0
    
    # Else, safe
    return 1

def part1(data):
    total = 0
    for report in data:
        total += analyse_part1(report)

    return total

# PART 2
# Function to analyse_part_2 and check polarities
def analyse_part_2(report, already_failed):
    # Polarity of jumps
    # +1 is a positive shift, -1 vice versa
    polarities = []
    
    # Loop through every jump and calculate the difference
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]

        # If difference is 0
        if diff == 0:
            # If not first failure
            if already_failed:
                return 0
            # If removing element passes
            elif analyse_part_2(report[:i] + report[i+1:], True):
                return 1
            else:
                return 0
            
        elif abs(diff) > 3:
            # If not first failure
            if already_failed:
                return 0
            # If removing either element passes
            elif analyse_part_2(report[:i+1] + report[i+2:], True) or analyse_part_2(report[:i+0] + report[i+1:], True):
                return 1
            else:
                return 0
        
        # Keep track of polarities
        polarities.append(int(diff/abs(diff)))

    # Check polarities
    polarity_errors = (len(polarities) - abs(sum(polarities))) / 2

    # If more than 1, fail
    if polarity_errors > 1:
        return 0
    # If not first failure, fail
    elif polarity_errors == 1 and already_failed:
        return 0
    # If first failure
    elif polarity_errors == 1 and not already_failed:
        
        # Find index of wrong polarity
        if sum(polarities) > 0:
            index = polarities.index(-1)
        else:
            index = polarities.index(1)

        # If removing either element causes pass
        if analyse_part_2(report[:index] + report[index+1:], True) or analyse_part_2(report[:index+1] + report[index+2:], True):
            return 1
        else:
            return 0
    # If no polarity failures
    else:
        return 1
    

def part2(data):
    total = 0
    for report in data:
        total += analyse_part_2(report, False)

    return total

# Input file handling
file = open("input.txt", "r")

data = []
for line in file.readlines():
    line = list(map(int, line.strip("\n").split(" ")))
    data.append(line)

print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
