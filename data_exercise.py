# File Exercises
# Author:
#

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    x = f.readline()
    

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.
with open("./data_example.csv", encoding="utf-8") as f:
    x = f.readline()
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
with open("./data_example.csv", encoding="utf-8") as f:
    x = f.readline()
    for line in f:
        print(line)
# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.
with open("./data_example.csv", encoding="utf-8") as f:
    x = f.readline()
    for line in f:
        line_list = line.split(",")
        print(line_list)

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.
with open("./data_example.csv", encoding="utf-8") as f:
    x = f.readline()
    chicken_A = "Chicken Adobo"
    people_like_chicken = 0
    for likes in f:
        if chicken_A in likes:
            people_like_chicken += 1
    print(f"{people_like_chicken} likes chicken adobo")

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".
names_list = []
with open("./data_example.csv", encoding="utf-8") as f:
    x = f.readline()
    letter_starts_A = 0
    for line in f:
        A = line.split(",")
        names= A[0]
        first_letter = names[0]
        if first_letter == "A":
            letter_starts_A += 1
print(f"{letter_starts_A} people's name starts with an A")


        

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?
city_list= []
with open("./data_example.csv", encoding="utf-8") as f:
    x = f.readline()
    big_city = ["Guangzhou\n"]
    guangzhou = 0
    for line in f:
        A = line.split(",")
        for item in big_city:
            if item in A:
                guangzhou += 1
    print(f"{guangzhou} people come from guangzhou")

# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int

card_num = []
last_digits_that_are_even = 0
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        A = line.split(",")
        cards = A[3]
        card_num.append(cards)
    for cards in card_num:
        last_digit = cards[-1]
        if last_digit == "0" or last_digit == "2" or last_digit == "4" or last_digit == "6" or last_digit == "8":
            last_digits_that_are_even += 1
    print(f"{last_digits_that_are_even} people have even credit card number")
  
  
  # Herman helped me with this one :()


# Problem 8*:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?
