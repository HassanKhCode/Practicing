# lst = [0, 1, 2, 3, 4, 5, 6, 7]
# for n in range(len(lst)-1, -1, -1):
#     print(n, end=" ")

# print("Please enter 10 dates")
# dates = []
# for i in range(0, 10):
#     dates.append(input("Enter date: "))
#
# winter = 0
# spring = 0
# summer = 0
# autumn = 0
# winter_dates = []
# spring_dates = []
# summer_dates = []
# autumn_dates = []
# for date in dates:
#     if int(date[3]) == 1:
#         if int(date[4]) == 2:
#             winter += 1
#             winter_dates.append(date)
#         else:
#             autumn += 1
#             autumn_dates.append(date)
#     else:
#         if 2 >= int(date[4]):
#             winter += 1
#             winter_dates.append(date)
#         elif 5 >= int(date[4]) >= 3:
#             spring += 1
#             spring_dates.append(date)
#         elif 8 >= int(date[4]) >= 6:
#             summer += 1
#             summer_dates.append(date)
#         else:
#             autumn += 1
#             autumn_dates.append(date)
# print(f"You entered {winter} dates in winter: \n"
#       f"{winter_dates}")
# print(f"You entered {spring} dates in spring: \n"
#       f"{spring_dates}")
# print(f"You entered {summer} dates in summer: \n"
#       f"{summer_dates}")
# print(f"You entered {autumn} dates in autumn: \n"
#       f"{autumn_dates}")


# num = int(input())
# sum = 1
# if num == 0:
#     print("Factorial result: 1")
# elif num < 0:
#     print("Can't calculate negative numbers")
# else:
#     for n in range(1, num + 1):
#         sum = sum * n
#     print(f"Factorial result for inserted number: {sum}")

# num = int(input())
# for n in range(1, 11):
#     print(format(f"{n} * {num} = {n * num}",'>15'))

# num = int(input())
# for n in range(1, num + 1):
#     print(f"Current Number is: {n} and the cube is: {n * n * n}")

# n = int(input())
# sum = 0
# result = 0
# for i in range(0, n):
#     sum = sum * 10 + 2
#     result += sum
# print(result)

# n = int(input())
# squared_numbers = []
# sum = 0
# for i in range(1, n + 1):
#     sum += i**2
#     squared_numbers.append(i**2)
# print(squared_numbers)

# n = int(input())
# for i in range(1, n + 1):
#     print(f"* " * i)
# for i in range(n-1, -1, -1):
#     print(f"* " * i)

# various = ['AAA', [4, 5, 7], "5", 5, 3.0, True, 2654, -4, 0]
# for i in various:
#     if isinstance(i, bool):
#         continue
#     if isinstance(i, int) and i > 0:
#         print(i)

# for n in range(1, 51):
#     if n % 5 == 0 and n % 3 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         print(n)

# rows = int(input("Number of Rows:"))
# Columns = int(input("Number of Columns"))
# for r in range(1, rows + 1):
#     print(f"$" * Columns)

n = int(input("Enter number: "))
for i in range(1, n + 1):
    for j in range(0, i):
        print(i, end="")
    print()