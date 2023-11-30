EE# Syntax Errors
These types of errors are ones that occur when you run your code and then it breaks

they are relatively easy to spot and fix

Syntax errors occur when we dont follow the rules of the language completely
# Semantic Errors

Semantic errors occur when our code doesnt mean what we intend it to mean

These in Mr Ubials opinion are FAR MORE challenging to spot and fix

```python
user_response = input("DO you like to eat food?")

if user_response == "yes":
	print("you are a Human")
else: 
	print("you are some sort of robot")
```

the problem with the code above is subtle. what i (mr ubial) mean is that every anwser of yes should go into the yes block

```python
user_response = input("DO you like to eat food?")

if user_response.lower() == "yes":
	print("you are a Human")
else: 
	print("you are some sort of robot")