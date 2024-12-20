# SOLUTION FOR ADVENT OF CODE 2024 DAY 5

# Link https://adventofcode.com/2024/day/5

def build_rule_dict(rules):
    # Build a rule dictionary of dependencies
    # Key = page index, Value = Array of pages that must come before it i.e. it is dependent on
    rule_dict = {}

    for rule in rules:
        # If key exists, append
        if rule[1] in rule_dict.keys():
            rule_dict[rule[1]].append(rule[0])
        # Else create array
        else:
            rule_dict[rule[1]] = [rule[0]]

    return rule_dict


def check_valid(update, rule_dict):
    # Check if page order is valid according to rules
    for i in range(len(update)):

        # Is page dependent on anything (does it's entry in rule_dict exist)
        if update[i] in rule_dict.keys():
            required_before = rule_dict[update[i]]

            # Loop through all pages after and see if they should come before
            for j in range(i, len(update)):
                if update[j] in required_before:
                    return False
            
    return True


def unit_sort(rule_dict, to_sort):
    # to_sort is array containing 2 numbers ordered, [num1,num2]
    num1 = to_sort[0]
    num2 = to_sort[1]

    # If num1 has no prerequesites, it can come first
    if not num1 in rule_dict.keys():
        return 1
    
    # If num2 has no prerequesites, it can come first
    elif not num2 in rule_dict.keys():
        return 2

    # If rule_dict[num1] contains num2 then num2 is a prerequesite, and num2 > num1
    elif num2 in rule_dict[num1]:
        return 2
                
    # If rule_dict[num2] contains num1 then num1 is a prerequesite, and num1 > num2
    elif num1 in rule_dict[num2]:
        return 1
    
    # Otherwise, no specified order
    else:
        return 1


def merge_sort(rule_dict, update):

    # Get size
    size = len(update)

    # Recursive case
    # If larger than 2, half and then sort
    if size > 2:
        list1 = merge_sort(rule_dict, update[:size//2])
        list2 = merge_sort(rule_dict, update[size//2:])

        # Combine sorted lists
        output_list = []
        for i in range(size):
            if len(list1) == 0:
                output_list += list2
                break
            elif len(list2) == 0:
                output_list += list1
                break
            elif unit_sort(rule_dict, [list1[0], list2[0]]) == 1:
                output_list.append(list1.pop(0))
            else:
                output_list.append(list2.pop(0))

        return output_list

    # Base case 1, edge case
    elif len(update) == 1:
        return update

    # Base case 2, if only 2 values then sort
    else:
        if unit_sort(rule_dict, update) == 1:
            return update
        else:
            return [update[1], update[0]]


# Part 1
def part1(rule_dict, updates):
    total = 0

    # Loop through all updates, and get middle value of valid updates
    for update in updates:

        if check_valid(update, rule_dict):
            total += int(update[int(len(update)/2)])

    return total

# Part 2
def part2(rule_dict, updates):
    total = 0

    # Loop through all updates, and get middle value of resorted, invalid updates
    for update in updates:

        if not check_valid(update, rule_dict):
            sorted = merge_sort(rule_dict, update)
            total += int(sorted[int(len(sorted)/2)])

    return total

# Filehandling
# Note this assumes you've manually split the input file into 2 seperate files
folder = "input"

file = open(f"{folder}/rules.txt")
rules = [line.strip("\n").split("|") for line in file.readlines()]

file = open(f"{folder}/pages.txt")
updates = [line.strip("\n").split(",") for line in file.readlines()]

rule_dict = build_rule_dict(rules)

print(part1(rule_dict, updates))
print(part2(rule_dict, updates))

