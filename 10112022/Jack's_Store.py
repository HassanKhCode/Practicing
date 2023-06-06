amount_science_fiction = int(input())
amount_comics = int(input())
amount_history = int(input())
before_discount_price = amount_science_fiction * 58\
              + amount_comics * 32\
    + amount_history * 24
discount = 0
total_price = 0
if amount_science_fiction >= 3:
    discount += (amount_science_fiction * 58) * 0.1
if amount_history >= 3:
    discount += (amount_history / 3) * 24
total_price = before_discount_price - discount
if before_discount_price > 300:
    discount += 20
    total_price -= 20

print(f"Price before the discount: {before_discount_price}")
print(f"Discount total: {discount}")
print(f"Your final price is: {total_price}")
