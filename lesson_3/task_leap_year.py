# year = int(input())
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('It is a leap year')
# else:
#     print('It is not a leap year')
# if (year < 1900) or (year > 100000 ):
#
#  print(("year"), "It is False")
import calendar
year = int(input("Enter the year: "))
value = calendar.isleap(year)
if value == True:
    print("% s is a Leap Year" % year)
else:
    print("% s is not a Leap Year" % year)