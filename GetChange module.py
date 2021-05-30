def GetChange(p,n,d,q):
  total = float()
  p = p * 0.01
  print(p)
  n = n * 0.05
  print(n)
  d = d * 0.10
  print(d)
  q = q * 0.25
  print(q)
  total = (p + n + d + q)
  print(total)
  if total == 1:
    return "CONGRATULATIONS"
  else:
    return "TRY AGAIN"

pennies = int()
nickels = int()
dimes = int()
quarters = int()
result = str()

int(input("Pennies:"))
int(input("Nickels:"))
int(input("Dimes:"))
int(input("Quarters:"))

result = GetChange(pennies, nickels, dimes, quarters)
print(result)
