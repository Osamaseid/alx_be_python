price_amount = float(input("Enetr the price:"))

if price_amount >= 100:
 discount = 0.1 # 10%
elif price_amount >= 500:
 discount = 0.05 # 5%
else:
 discount = 0

discount_price = price_amount * (1 - discount )
print(f"the discounted amount is:{discount_price}")
