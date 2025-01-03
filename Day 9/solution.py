# SOLUTION FOR ADVENT OF CODE 2024 DAY 9

# Link https://adventofcode.com/2024/day/9

def part1(data):
    # Collect aligned arrays of files and spaces
    files = [int(data[i]) for i in range(0, len(data), 2)]
    spaces = [int(data[i]) for i in range(1, len(data)-1, 2)]

    # The algorithm works by building the disk left to right
    # When it comes to filling in blank spaces, it takes from the end of the files
    # Where it last took from is tracked using end_pointer
    # Where it has built to is tracked using start_pointer
    start_pointer = 0
    end_pointer = len(files)-1


    # start_pointer needs to be used twice per increment, once for files once for pointer
    # Boolean flip-flop that tells algorithm which it's used
    isFile = True

    disk = []
    while start_pointer <= end_pointer:
        
        if isFile:
            # Add as many digits as stated in input file
            disk += [start_pointer] * files[start_pointer]

            # Edge case for final run of algorithm, after disk is defragmented want to ignore all spaces after
            if start_pointer == end_pointer:
                break

        else:
            # Until spaces == 0, keep taking off from end of files
            while spaces[start_pointer] > 0:
                

                # If there are enough spaces to completely fit the remainder of a file in, do so
                if files[end_pointer] <= spaces[start_pointer]:
                    # Add to disk
                    disk += [end_pointer] * files[end_pointer]

                    # Update remaining spaces
                    spaces[start_pointer] -= files[end_pointer]
                    
                    files[end_pointer] = 0

                    # Move end pointer
                    end_pointer -= 1

                # Elif there aren't enough, take as many as possible
                elif files[end_pointer] > spaces[start_pointer]:
                    # Add to disk
                    disk += [end_pointer] * spaces[start_pointer]

                    # Update remaining fragments from end file
                    files[end_pointer] -= spaces[start_pointer]

                    spaces[start_pointer] = 0

            start_pointer += 1

        # Flip-flop
        isFile = not(isFile)

    # Checksum
    total = 0
    for i in range(len(disk)):
        total += i * int(disk[i])

    return total


def part2(data):
    # This works in blocks, and reorders the disk one by one
    # Each file is kept as an object in the "disk" which is an ordered list

    # Flip flop for building initial datastructure
    isFile = True
    i = 0
    drive = []

    for value in data:
        if isFile:
            # File format:
            # [ID, Length, Attempted to move yet (bool)]
            drive.append([i, int(value), False])
        else:
            # Space format:
            # [".", Length]
            drive.append([".", int(value)])
            i += 1

        isFile = not isFile

    # Reverse, as I'm inserting values so makes easier with indexing
    drive = drive[::-1]

    i = 0
    while i < len(drive):

        # If it's a file
        if drive[i][0] != ".":

            # That we haven't tried to move yet
            if not drive[i][2]:
                # Loop back to the start
                for j in range(len(drive)-1, i, -1):
                    # If it's a space
                    if drive[j][0] == ".":

                        # Perfect fit
                        if drive[j][1] == drive[i][1]:
                            # Replace like-for-like
                            drive[j] = drive[i]
                            drive[i] = [".", drive[i][1]]

                            # Set visited to true
                            drive[j][2] = True

                            break
                        
                        # Hole is slightly oversized
                        elif drive[j][1] > drive[i][1]:
                            # Shortern spaces in new slot
                            drive[j][1] -= drive[i][1]

                            # Store old block
                            temp = drive[i]
                            temp[2] = True

                            # Replace with spaces
                            drive[i] = [".", drive[i][1]]

                            # Insert new spacing
                            drive.insert(j+1, temp)

                            break

        # Counter increase         
        i += 1

    # Reassemble drive
    drive = drive[::-1]
    output = []

    for section in drive:
        if section[0] == ".":
            output += ["."] * section[1]
        else:
            output += [section[0]] * section[1]

    # Checksum
    total = 0
    for i in range(len(output)):
        if output[i] != ".":
            total += i * output[i]

    return total

# File formatting
data = open("input.txt", "r").readline().strip("\n")

print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")