# Format Strings
we can evaluate inside of strings using f-strings
To create an f-string, we put an f before the opening quote

```python
fave_food = input("what is your favourite food?")

print(f"Oooof {fave_food} sounds good)
```

# String Methods

[[methods]] are function we can use on [[objects]].

String methods allow us to modify and work with string

Say for example, we want to make all charecters of a string lowercase

```python
mr_ubial_yelling = "PLEASE PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower()) # lowercases the letters

```

## .`lower()`

the .lower method takes a string and converts all UPPERCASE charecters to lowercase
The .lower() method takes a string and converts all UPERCASE  characters tp help with [[Errors]]

## .upper()

THe .upper() method converts all lowercase chrecters to uppercase in a string

## `.strip(str)` 
the `.strip()` method removes charecters from the beginning and ned of the string

```python

# good, GOod, GOOD GOOD! good. good?
user_feeling = input("HOw are you feeling?")

if  user_feeling.lower().strip("!.,?") == "good":
	print("thats great")
```

## .split(str) -> List

the .split() method splits a string into a [[Lists]], seperating the string based on the charecters you give it

```python

grocery_str = "eggs milkcheese hotwheels"

grocery_list = grocery_str.split(" ")
```



