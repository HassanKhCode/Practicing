layout = input("Please implement the layout of the aircraft")
split_layout = layout.split(" ")
if len(split_layout) == 3:
    left_seats = len(split_layout[0])
    middle_seats = len(split_layout[1])
    right_seats = len(split_layout[2])
    print(f"Number of seats on each side {left_seats} - {middle_seats} - {right_seats}")
if len(split_layout) == 2:
    left_seats = len(split_layout[0])
    right_seats = len(split_layout[1])
    print(f"Number of seats on each side {left_seats} - {right_seats}")

seat_number = input("Enter seat number")
if seat_number[1].isdigit():
    row = seat_number[0]
    row += seat_number[1]
    char = seat_number[2]
else:
    row = seat_number[0]
    char = seat_number[1]
print(f"Row number: {row} \n"
f"char number: {char} ")