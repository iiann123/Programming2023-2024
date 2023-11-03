name = input("hi traveller, what is your name")

total_continents = 0

continents = ['Asia', 'South America', 'North America', 'Africa', 'Europe', 'Antarctica', 'Australia']

print(f"nice to meet you {name}")


for cont in continents:
    value = input(f"have you been to {cont}")
    if value.lower().strip(",.?!") == "yes":
        total_continents += 1

print(f"you have been to {total_continents} continents")