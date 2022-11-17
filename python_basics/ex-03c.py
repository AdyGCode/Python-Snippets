# Exercise 1
# Write a Python program that:
#
# asks the user for their first name,
# asks the user for their last name,
# prints a message that says something like:
#   ‘Nice to meet you, <first_name> <last_name>.’
#

# To convert a line to a comment - CTRL+/ (toggle line as a comment)

given_name = input("What is your first name: ")

# duplicate current line (or selection) CTRL+D
family_name = input("What is your last name: ")

print(f"nice to meet you {given_name} {family_name}")

# Exercise 2
# After showing the greeting:
# Ask the user for a number
# If the number is negative, show message indicating it is too small
# If the number is > 100, show a message indicating it is too large
# Otherwise, just say “thanks!”

number = int(input("Enter a number between 0 and 100 inclusive: "))
if number < 0:
    print("Number is too small, it must be zero or more")
if number > 100:
    print("Number is too big, it must be 100 or less")
# if number >= 0 and number <= 100:
# if number in range(0, 101):
if 0 <= number <= 100:
    print('Thanks!')

# CTRL + ALT + L is reformat code (or selected code)

# Exercise 3
# If the user entered a positive number that is <= 100:
# Create a loop that counts down
# It should print “<n> bottles of beer”
# The last line might read “1 bottle of beer” (singular *)

for count in range(number, 0, -1):
    message = f"{count} bottle{['s', ''][0 if count > 1 else 1]} of " \
              f"beer"
    print(message)
