# import argv from the sys module
from sys import argv
# set script and filename variables from the script arguments
script, filename = argv
# open the filename passed in as an argument, and assign the file object to the text variable
txt = open(filename)
# print a string with the filename
print(f"Here's your file {filename}:")
# print the contexts of the txt file object
print(txt.read())
# print a string
print("Type the filename again:")
# prompt the user for a file name
file_again = input("> ")
# opent the file that the user entered, and then assign the file object ot the variable txt_again
txt_again = open(file_again)
# print the contents of the txt_again file object
print(txt_again.read())
