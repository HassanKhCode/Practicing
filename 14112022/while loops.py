# num = 1
# while num <= 10:
#     print(num)
#     num = num + 1

# num = int(input("Insert number: "))
# i = 1
# instance = 0
# while num > i:
#     print(i)
#     i = 3 + instance * 3
#     instance += 1

# special_char = '$'
# insertion = int(input())
# count = 0
# sum = 0
# while insertion != special_char:
#     sum += int(insertion)
#     count += 1
#     insertion = input()
# average = sum / count
# print(f"The sum is: {sum} and the average is: {average}")

# names_grades = [[],[]]
# name_and_grade = input()
# sum = 0
# while name_and_grade != "$$$":
#     names_grades[0].append(name_and_grade.split(" ")[0])
#     names_grades[1].append(name_and_grade.split(" ")[1])
#     sum += int(name_and_grade.split(" ")[1])
#     name_and_grade = input()
# print(f"Names: {names_grades[0]}, Average grade is: {sum / len(names_grades[1])}")

# num_str = 0
# num_char = 0
# num_digit = 0
# insertion = input()
# while insertion != '$':
#     if insertion.isdigit():
#         num_digit += 1
#     elif len(insertion) == 1:
#         num_char += 1
#     else:
#         num_str += 1
#     insertion = input()
# print(num_str, num_char, num_digit)

# str = input()
# n = 0
# string_length = len(str)
# same_size_count = 1
# while n < 10:
#     str = input()
#     if len(str) == string_length:
#         same_size_count += 1
#     n += 1
# print(same_size_count)

# num = int(input("insert number:"))
# while num % 2 == 0:
#     num = int(input("insert more:"))

# num = int(input())
# count = 0
# while num > 0:
#     count += 1
#     num = int(num / 10)
# print(count)

# num = int(input())
# rev_num = 0
# while num > 0:
#     rev_num += num % 10
#     num = int(num / 10)
#     if num > 0:
#         rev_num *= 10
# print(rev_num)
# num = str(input())
# print(num[-1::-1])

print("Hey welcome to the rock paper scissors game!. To start please enter your name:")
player1 = input("Player1: ")
player2 = input("Player2: ")
print("The game has started in order to exit type (exit)")
total_rounds = 0
player1_wins = 0
player2_wins = 0
total_draws = 0
player1_move = input("Player1's turn choose between rock/paper/scissors: ")
player2_move = input("Player2's turn choose between rock/paper/scissors: ")
while player1_move != "exit" or player2_move != "exit":
    total_rounds += 1
    if player1_move == "rock" and player2_move == "scissors"\
            or player1_move == "paper" and player2_move == "rock"\
            or player1_move == "scissors" and player2_move == "paper":
        print("Player 1 Wins!")
        player1_wins += 1
    elif player1_move == player2_move:
        print("It's a Draw!")
        total_draws += 1
    else:
        print("Player 2 Wins!")
        player2_wins += 1
    player1_move = input("Player1's turn choose between rock/paper/scissors: ")
    player2_move = input("Player2's turn choose between rock/paper/scissors: ")
print(f"Total Rounds: {total_rounds}")
print(f"{player1} total wins: {player1_wins}")
print(f"{player2} total wins: {player2_wins}")
print(f"Total Draws: {total_draws}")