# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(1, 10, 2):
#     print(my_list[i], end=" ")

# cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
# country = ['USA', 'Ukranie', 'France', 'UK', 'Israel']
# for i in range(0, len(cities)):
#   print(f"{country[i]} - {cities[i]}")

# names = ["Saba", "Franke", "3amo", "Max"]
# new_names = []
# for name in names:
#     new_names.append("Dr. " + name)
# print(new_names)

# types = ['AAA', [4, 5, 7], "5", 5, 3.0, True, 2654, -4, 0]
# for i in types:
#     print(f"{i} {type(i)}")

# l1 = [54, -1, 45, 987, 5, 2, 65, 7, 12]
# max_num = l1[0]
# second_max = 0
# for num in l1:
#     if num > max_num:
#         max_num = num
#     if second_max < num < max_num:
#         second_max = num
# print(max_num, second_max)

num = int(input())
for n in range(1, num+1):
    print(n, end=" ")