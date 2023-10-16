#Ian Weng
# 10/16
# starwars bot

import time

print("I will decide if you can join the darkside")
time.sleep(1)

fav_color = input("do you like the color red")
cape = input("do you like capes?")

if fav_color.lower().strip(",. ?!") == "yes":
    print("dark side you are")
elif cape.lower().strip(",. ?!") == "yes":
    print("dark side you are")
else: 
    print("light side")
