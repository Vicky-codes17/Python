leap_year = int(input("Enter the number : "))
n = leap_year
if n%4 ==0 and n%100 == 0 and n%400 == 0:
    print("It is leap year")
else:
    print("Not a leap year")