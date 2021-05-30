def GetDiscount(price, discount, days):
  diff = float()
  totaldiff = float()
  diff = price * discount
  for i in range(0,days):
      diff = price * discount
      price = price - diff
  price = round(price, 2)  
  return price

price = float()
discount = float()
days = int()

price = float(input())
discount = float(input())
days = int(input())

total = GetDiscount(price, discount, days)
print(total)
