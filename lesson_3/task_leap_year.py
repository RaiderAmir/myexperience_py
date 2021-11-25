import calendar
year = int(input("Enter the year: "))
value = calendar.isleap(year)
if value == True:
    print("% s is a Leap Year" % year)
else:
    print("% s is not a Leap Year" % year)