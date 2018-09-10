# create a variable called formatter, which is a string made of 4 formatting characters
formatter = "{} {} {} {}"
#prints formatter with 4 digits
print(formatter.format(1, 2, 3, 4))
#prints formatter with 4 strings
print(formatter.format("one", "two", "three", "four"))
#prints formatter with 4 booleans
print(formatter.format(True, False, False, True))
#prints formatter with itself, 4 times
print(formatter.format(formatter, formatter, formatter, formatter))
#prints formatter with 4 strings
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
# It uses both double and single quotes, one of the lines has an apostrophe in it
