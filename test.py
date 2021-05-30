num_days = int()
num_weeks = int()
snow_fall = float()
daily_total = float()
weekly_total = float()

for num_weeks in range(1,3):
    for num_days in range(1,4):
        snow_fall = float(input("Enter how much snow has fallen: "))
        daily_total = daily_total + snow_fall
    print("Total Daily Snowfall: ", daily_total)
    weekly_total = weekly_total + daily_total
print("Total Weekly Snowfall: ", weekly_total)

