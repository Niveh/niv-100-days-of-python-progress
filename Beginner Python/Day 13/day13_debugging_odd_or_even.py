# Original Code:

# number = int(input("Which number do you want to check?"))
# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Fixed Code:
number = int(input("Which number do you want to check?"))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Issue: first "if" statement typo, used assignment "=" instead of comparison "=="
