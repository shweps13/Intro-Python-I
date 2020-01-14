"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("============================")
print("Today is", dt_string)	
print("============================")

c = calendar.TextCalendar(calendar.SUNDAY)
def calend (m=None, y=None):
  if m is None and y is None:
     str = c.formatmonth(now.year, now.month)
     print(str)
  elif type(m) is not int or type(y) is not int:
     print("Please, make sure that input data is correct")
     print("You need to put month and year, like '5, 2017' for May 2017")
  elif m <= 0 or m > 12:
     print("Please, check format of the month")
  elif type(m) is int and y is None:
     str = c.formatmonth(now.year, m)
     print(str)
  elif y < 0:
     print("Sorry, but year cannot be less than 0")
  elif type(m) is int and type(y) is int:
     str = c.formatmonth(y, m)
     print(str)
  else:
     print("Please, make sure that input data is correct")

calend(6, 2019)