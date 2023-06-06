# word = input("please enter a word: ")
# print(f"that word's length is: {len(word)}")

check = True
string = input("Enter anything and I will check if it's palindrome or not here: ")
for i in range(0, int(len(string)/2)):
    if string[i] != string[len(string)-i-1]:
        check = False
        print("Not a palindrome")
if check:
     print("Palindrome!")
