"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("Number of arguments: ", len(sys.argv))
print("=== And here there are ===")
for argument in sys.argv:
    print(argument)
print("=== End of the arguments ===")

# Print out the OS platform you're using:
if sys.platform.startswith('linux'):
    print("You using Linux")
elif sys.platform.startswith('darwin'):
    print("You using MacOS")
elif sys.platform.startswith('win32'):
    print("You using Windows")
elif sys.platform.startswith('cygwin'):
    print("You using Windows/Cygwin")
elif sys.platform.startswith('aix'):
    print("You using Aix")

# Print out the version of Python you're using:
print("Python version is: ", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("The process ID is:", os.getpid())

# Print the current working directory (cwd):
print("The working directory:", os.getcwd())

# Print out your machine's login name
print("Machine's name:", os.uname()[4])
