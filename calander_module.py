import calendar
y=int(input("Enter an year:\n"))
m=int(input("Enter a month:\n"))
print(calendar.month(y,m,w=6))
a=calendar.calendar(firstweekday=2)
print(a.itermonthdays(y,m))
