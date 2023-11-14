person1_hobbies = input("please enter hobbies, seperated by spaces").lower()
person2_hobbies = input("please enter hobbies, seperated by spaces").lower()
sim_score = 0


p1 = person1_hobbies.split()
p2 = person2_hobbies.split()

for hobbies in p1:
    if hobbies in p2:
        sim_score += 1

print(f"person1: {person1_hobbies}")
print(f"person2: {person2_hobbies}")
print(f"you have {sim_score} hobbies in common")
