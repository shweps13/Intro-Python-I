# Write a function is_even that will return true if the passed-in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even(x):
    if (x % 2) == 0:
        print("{0} is Even".format(x))
        return True
    else:
        print("{0} is Odd".format(x))

is_even(num)