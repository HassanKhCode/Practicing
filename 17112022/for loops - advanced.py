# goods = [['apple', 'pear', 'peach', 'chery'], ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
#                                                'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]
# longest_words = []
# index = []
# word_length = 0
# for i, good in enumerate(goods):
#     for i2, goo in enumerate(good):
#         if len(goo) > word_length:
#             longest_words = [goo]
#             index = []
#             index.append((i, i2))
#             word_length = len(goo)
#         elif len(goo) == word_length:
#             longest_words.append(goo)
#             index.append((i, i2))
# vowels = "aeoiu"
# vowel_count = 0
# for word in longest_words:
#     for letter in word:
#         if letter in vowels:
#             vowel_count += 1
# print(longest_words, index, vowel_count)

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print("* ", end="")
        k += 1

    k = 0
    print()

