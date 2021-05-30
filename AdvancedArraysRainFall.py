def RainFall(days):
    rain_fall = float()
    index = int()
    days_array = [0 for i in range(days)]
    for i in range(0, days):
        rain_fall = float(input())
        days_array[index]=rain_fall
        index = index + 1
    print(days_array)


def main():
    days = int()
    days = int(input())
    RainFall(days)

main()
