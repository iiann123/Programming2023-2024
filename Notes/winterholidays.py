# winter holiday review
# Ian weng
# 8 jan 2024

# create a function called winter_holiday
# take one parameter
# string
# return a summary of an event from you holidays
import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our windter holidays 2023/24
    Params:
        good_or_bad - indicate what kind of event to summarize
        
    Returns: 
        an event that happened durin the holidays"""
  
    good = ["I went to eat!", "I got NL pool", "I went out with my friends"]
    good_rdm = random.choice(good)

    
    bad = [" was tired Zzzzzzzz", "body is sore", "I hate swimming"]
    bad_rdm = random.choice(bad)

    if good_or_bad.lower().strip() == "good":
        return good_rdm
    if good_or_bad.lower == "bad":
        return bad_rdm
   
def main() -> None:
    response = input("how was your winter holiday?")
    print(winter_holiday(response))


#sdadas
    
if __name__ == "__main__":
    main()