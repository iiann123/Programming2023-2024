# Ian Weng
total = 0
ans1 = input("Did you eat?").lower()
ans2 = input("Did you study?").lower()
ans3 = input("did you do your laudry").lower()
ans4 = input("did you call grandma?").lower()


if ans1 == "yes":
    total += 1
if ans2 == "yes":
    total += 1
if ans3 == "yes":
    total += 1
if ans4 == "yes":
    total += 1
    
if total == 0:
    print("Im coming over")
elif total <= 2:
    print("OK")
elif total <= 4:
    print("GOOD")