def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# test the return value of isequal()
num1 = 40
num2 = 50
num3 = 50

print(isequal(num1, num2))
print(isequal(num2, num3))


# A new puzzle.
print("Here is a new puzzle.")

# write a simple formula and use the function again
uplen = 50
downlen = 100
height = 80
what_again = divide(multiply(height, add(uplen, downlen)), 2)

print("That become: ", what_again, "Bazinga!")
