year = int(input("Enter Year:"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")
# write a python programme to calculate the ticket price of a therter based on age
# 0-5 free
# 0-12 500
# 13-17 1000
# 18+ 1500+