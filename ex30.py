# assigning people variable to 30
people = 30
# assinging cars variable to 40
cars = 40
# assigning trucks variable to 15
trucks = 15

# if cars are more than people
if cars > people:
# print a string
    print("We should take the cars.")
# unless cars are less than people
elif cars < people:
# then print this string
    print("We should not take the cars.")
# if cars are equal to people
else:
# print this string
    print("We can't decide.")
# if trucks are more than cars
if trucks > cars:
# print this string
    print("That's too many trucks.")
# if trucks are less than cars
elif trucks < cars:
# print this string
    print("That's too many trucks.")
# if cars are equal to trucks
else:
# print this string
    print("We still can't decide.")
# if people are more than trucks
if people > trucks:
# print this string
    print("Alright, let's just take the trucks.")
# if trucks are <= to people
else:
# print this string
    print("Fine, let's stay home then.")
