relative_path = "C:\\Users\hanfa\PycharmProjects\Practicing\AAPL.csv"
absulote_path = "C:\\Users\\hanfa\\PycharmProjects\\Practicing\\alic_in_wonderland.txt"
min = None
with open(relative_path, "r") as fd:
    fd.readline()
    for line in fd:
        low = float(line.split(",")[1])
        if low != None and low < min:
            min = low
print(min)
