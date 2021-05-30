#Variables
weekly_savings = float()
monthly_savings = float()
total_savings = float ()

#outer loop
for months in range (1,6):
  #inner loop
  for weeks in range (1,4):
    weekly_savings = int(input("Weekly Savings:"))
    monthly_savings = monthly_savings + weekly_savings
  #end inner loop
  print("Monthly Savings:", monthly_savings)
  total_savings = total_savings + monthly_savings
  print("Total Savings:", total_savings)
  monthly_savings = 0.0
#end loop
