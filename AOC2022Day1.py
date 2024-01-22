#Aoc day 1
# Ian
#Nov 30 2023

# there is one elf carrying the most calories 
# Howmany does that one have

# create a list that holds all the calories of the elves
elves = []

# open the file
with open("./AOC2022Day1.txt") as f:
    # calories of the current elf
    current_cals = 0
    for line in f:
        # if there is something in the line
        if line.strip():
            current_cals += int(line.strip())
        else: 
            #dump current cals into elves list
            elves.append(current_cals)
            # reset current cals for next elf
            current_cals = 0

# find the biggest calories in the list
biggest_cals = 0
for elf in elves:
    if elf > biggest_cals:
        biggest_cals = elf
print(elves)
print(max(elves))
print(sorted(elves))

# get the top three and usm them

print(sum(sorted(elves)[-3: ]))