import string


# def sumoflist(nums: list) -> float:
#     sum = 0
#     for n in nums:
#         sum += n
#     return sum

# def multiply(tup: tuple) -> float:
#     sum = 1
#     for n in tup:
#         sum *= n
#     return sum

# def max(n1: float, n2: float, n3: float) -> float:
#     if n1 >= n2:
#         if n1 > n3:
#             return n1
#         else:
#             return n3
#     elif n2 > n1:
#         if n2 > n3:
#             return n2
#         else:
#             return n3

# def factorial(n: int) -> int:
#     sum = 1
#     for i in range(1, n + 1):
#         sum = sum * i
#     return sum
# print(factorial(6))

# def unique(tup: tuple) -> tuple:
#     new_tup = []
#     for i in tup:
#         if i not in new_tup:
#             new_tup.append(i)
#     return tuple(new_tup)
# print(unique((1,2,3,4,4,5,5,1)))

# def even(list: list):
#     for n in list:
#         if n % 2 == 0:
#             print(n)
#
# even([1,2,3,4,5,6])

# def isperfect(num: int) -> bool:
#     sum = 0
#     for n in range(1, (num // 2 + 1)):
#         if num % n == 0:
#             sum += n
#     if num == sum:
#         return True
#     else:
#         return False
# print(isperfect(496))

# def is_prime(num: int) -> bool:
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             return False
#     return True
# print(is_prime((7)))

# def reverse(string: str) -> str:
#     rev_str = ""
#     for char in string[-1::-1]:
#         rev_str += char
#     return rev_str
# print(reverse("fedcba"))

# def isinrange(num: int, start: int, end: int) -> bool:
#     for n in range(start, end + 1):
#         if num == n:
#             return True
#     return False
# print(isinrange(11,7,10))

def ispangram(sentence: str):
    check = string.ascii_lowercase
    sentence = sentence.lower()
    for char in check:
        if char not in sentence:
            return False
    return True
print(ispangram("The quick brown fox jumps over the lazy dog"))