'''
FOod suggestion bot 
Ian Weng
6 october 2023

a bot that asks the user what their favourite food is 
the bot identifies the type/cuisine of the food and offer a suggestion 
for a resteraunt

'''
import random
import time
import sys
# introduce the bot to the user
# ask the user what their favourite food is
sys.stdout.write("hello, i am here to suggest a resteraunt to you")
print("\n")
time.sleep(1)
fav_food = input("To help me suggest a resteraunt, tell me what your favourite foodi ")
# if they anwser with an italian dish
# sugeest an italian resteraunt
# list all the italian dishes
italian_food = ["pizza", "pasta", "canneloni", "tiramisu"]
jap_food = ["sushi", "ramen", "terriyaki", "miso soup"]
if fav_food.lower().strip(",.?! ") in italian_food:
    print("I think you might lke italian food ")
    time.sleep(1)
    print(" I suggest Bella Roma Italian Ristorante Richmond")
    time.sleep(1)
    print("You can find the address below:")
    print("8368 Alexandra Rd, richmond")
elif fav_food.lower().strip(", . ? ! ") in jap_food:
    print("I think you might lke japanese food ")
    time.sleep(1)
    sys.stdout.write(" Torake Japanese Cuisine")
    print("\n")
    time.sleep(1)
    sys.stdout.write("You can find the address below:")
    print("\n")
    sys.stdout.write("9471 No 2 Rd #130, Richmond, BC V7E 2C9 richmond")
else: print("My algorithim is still being worked on")
time.sleep(1)
sys.stdout.write(" thankyou for using this service")




