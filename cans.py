#Variables
daily_cans = int()
weekly_cans = int()
total_cans = int()

#outer loop keeping track of number of weeks
for weeks in range(1,3):
    #inner loop keeps track of days
    for days in range (1,4):
        daily_cans = int(input("Enter total cans collected today: "))
        weekly_cans = weekly_cans + daily_cans
    #end loop
    print("Total cans collected this week: ", weekly_cans)
    total_cans = total_cans + weekly_cans
    print("Total cans collected for the entire drive: ", total_cans)
    weekly_cans = 0
#end outer loop
