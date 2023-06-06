# #Question 5
# salary = float(input())
# name = input()
# tax = 0
# if salary <= 120000:
#     tax = salary - 46000
#     tax = 6900 + tax * 0.3
#     if salary <= 46000:
#         tax = salary - 23000
#         tax = 2300 + tax * 0.2
#         if salary <= 23000:
#             tax = salary * 0.1
# elif salary <= 220000:
#     salary -= 120000
#     tax = 29100 + salary * 0.4
# else:
#     salary -= 220000
#     tax = 69100 + salary * 0.5
# print(name, f"You need to pay {tax}$ in taxes")



# grade = int(input())
# if grade > 95:
#     print("Great!")
# elif grade >= 85 and grade <= 94:
#     print("Very Good!")
# elif grade <= 84 and grade >= 75:
#     print("Good")
# elif grade <= 74 and grade >= 65:
#     print("Almost Good")
# elif grade <= 64 and grade >= 55:
#     print("Enough")
# else:
#     print("Not Enough")



# A = float(input())
# B = float(input())
# C = float(input())
# D = float(input())
# E = float(input())
# F = float(input())
# if A * E - B * D == 0 or A * E - B * D == 0:
#     print("Equation has no solution")
# else:
#     x = (C*E-B*F) / (A*E-B*D)
#     y = (A*F-C*D) / (A*E-B*D)
#     print(f"x value is: {x}")
#     print(f"y value is: {y}")


# def check_leap_year(year: int):
#     if year % 4 == 0 and year % 100 != 0\
#             or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#        print("A Leap Year!")
#     else:
#       print("Not a Leap Year :(")
#
# year = int(input())
# month = int(input())
# if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
#     print("31 days!")
# elif month == 4 or 6 or 9 or 11:
#     print("30 days!")
# elif check_leap_year(year):
#     print("29 days!")
# else:
#     print("28")