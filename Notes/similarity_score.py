# calculating similariy score
# Author Ian
# 9/11/23

# Calculate similarity scores between two people

# create two lists that represent the movies that they like
ubials_fave_movies = [
    "the matrix", 
    "avengers: infinity war",
    "infernal affairs",
    "rogue one",
    "the empire strikes back"
]

similarity_score = 0

bens_fave_movies = [
    "thomas and friends, big world big adventure",
    "padington 2",
    "avengers: infinity war",
    "minions",
    "rogue one"
]

# For every movie in the first list
    # if that movie is in the second list
        # increse the similarit score by 1
for movie in ubials_fave_movies:
    if movie in bens_fave_movies:
        similarity_score += 1

print(f"your similarity score is {similarity_score}")

