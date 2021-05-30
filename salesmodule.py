#write your function here
def AvgSales(sales1, sales2, sales3):
  total_sales = float()
  total_sales = (sales1 + sales2 + sales3)
  avg = (total_sales / 3.0)
  return avg

#delcare variables
sales1 = float()
sales2 = float()
sales3 = float()
average = float()

#Get sales from the user
sales1 = float(input())
sales2 = float(input())
sales3 = float(input())

#write your code to call your function here
average = AvgSales(sales1, sales2, sales3)

#print out the average
print(average)
