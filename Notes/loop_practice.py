# IAn Weng
# 10/10
# Loop Practice

# create a list of groceries
groceries = ["hot wheels", "lego", "ice cream" ,"video games"]

# DO something for each thing in the list
# print it out in a pretty way

for item in groceries:
    print(f"*{item}")
    print("  ---")

    # create a [yramid using a for loop

star = ["*","**", "***", "****", "*****", "******"]
for item in star:
    print(f"{item}")


# Problem
#Create a new years eve countdpwn
# REquirements
# stars off at 10
# countdown everysecond
# instead of every zero it says happynew year
import time

numbers= ["10" , "9", "8", "7", "6", "5", "4", "3", "2", "1" ,"Happy New Year"]

for item in numbers:
    print(item)
    time.sleep(1)
   
    