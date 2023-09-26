"""
Chatbot
Ian Weng
sep21 2023
"""
import time
import random
# Greet the user
print("Hi my name is chatbot")
#pause between lines of dialoge
time.sleep(1.5)
#Get the users name and store it in a variable
User_name = input("What is your name")
# Respond with user's name
print(f" Nice to meet you {User_name}")
# Ask the user what their favourite food is
time.sleep(1.5)
fav_food = input("What is your favourite food?")
# Respond with something appopriate
print(f"I love {fav_food} as well! It is very yummy")
# Respond with something that is NOT TOO repetitive
favourite_food_responses = ["yum", "That sounds delicious" ,
                             f" {fav_food} is super delicous",
                              f"I love {fav_food} as well! It is very yummy" ]
#Crete a list of appropriate responses
random_response = random.choice(favourite_food_responses)
#Choose one response randomly from the list
print(random_response)
#Print out the chosen response

print(favourite_food_responses[2])