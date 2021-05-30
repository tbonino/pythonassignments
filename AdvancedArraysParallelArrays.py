def GetDays(months, days, user_month):
    index = int()
    month = str()
    day = int()
    search = str()
    validate = bool
    index = 0
    validate = False
    while validate == False and index < len(months):
        search = months[index]
        if search == user_month:
            validate = True
            month = months[index]
            day = days[index]
            return month, day
        else:
            index = index + 1
            validate = False

def main():
    months = ["December", "January", "February", "March"]
    days = [10, 8, 6, 11]
    mymonths = str()
    mydays = int()
    mymonths, mydays = GetDays(months, days, "January")
    print(mymonths, "had", mydays, "sunny days.")
main()
