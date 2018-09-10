#this is a variable
types_of_people = 10
#this is a string with interpolation
x = f"There are {types_of_people} types of people."
#these are more variables
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#these print commands are printing the above variables
print(x)
print(y)
#these print commands are formatting the variables into the strings
print(f"I said: {x}")
print(f"I also said: '{y}'")
#these are variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#this is a print command with a formatted variable interpolated
print(joke_evaluation.format(hilarious))
#these are variables
w = "This is the left side of..."
e = "a string with a right side."
#this is printing the two strings that are variables and combining them.
print(w + e)
