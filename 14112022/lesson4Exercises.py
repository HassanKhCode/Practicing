list = [['Paris', 'London', 'New York'], [45, True, 5.5, 'hello'],
                -3, [5, ['#', '$', '%', '^', [10, 20, 30 ,40]]],
        [['a'], ['b'], 'c', [['d']]]]
print(list[2])
print(list[1][2])
print(list[0])
print(list[1], list[2])
print(list[3][1][3])
print(list[4][0][0])
print(list[4][1])
print(list[4][3][0][0])
print(list[3][1][4][1:5:2])
print(list[3][1][-2::-3])

data = 0
print("Insert data here, when you finish Enter '$'")
while data != '$':
    data = input("Enter: ")
print("Thanks!")