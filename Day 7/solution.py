# SOLUTION FOR ADVENT OF CODE 2024 DAY 7

# Link https://adventofcode.com/2024/day/7

def dfs(target, current_value, nums):

    # Base cases
    # If overshot, then path is wrong
    if target < current_value:
        return False
    
    # If used all numbers
    if len(nums) == 0:
        # If is exactly target
        if target == current_value:
            return True
        
        # Else equation is wrong
        else:
            return False

    # Else recurse with next value
    elif len(nums) >= 1:

        # Addition
        if dfs(target, current_value + nums[0], nums[1:]):
            return True

        # Multiplication        
        if dfs(target, current_value * nums[0], nums[1:]):
            return True
        
        # Part 2
        # Concatenation
        if part2_enabled:
            if dfs(target, concatenate(current_value, nums[0]), nums[1:]):
                return True
        
        return False


def concatenate(num1, num2):
    return int(str(num1) + str(num2))

        
def main(equations):
    total = 0

    # Loop through all equations
    for target, numbers in equations:
        # Check
        if dfs(target, numbers[0], numbers[1:]):
            total += target

    return total


# File handling
file = open("input.txt", "r")

equations = []
for line in file.readlines():
    target, numbers = line.strip("\n").split(": ")
    target = int(target)
    equations.append([target, list(map(int, numbers.split()))])


part2_enabled = False
print(f"Part 1: {main(equations)}")

part2_enabled = True
print(f"Part 2: {main(equations)}")

