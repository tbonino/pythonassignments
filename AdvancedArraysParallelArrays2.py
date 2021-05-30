def FindHighest(names,calls):
    index = int()
    name_value = str()
    call_value = int()
    search = int()
    highest_calls2 = int()
    highest_name2 = str()
    index = 0
    highest_calls2 = calls[0]
    for index in range(0, len(calls)):
        search = calls[index]
        if search > highest_calls2:
            highest_calls2 = search
            highest_name2 = names[index]
    return highest_name2, highest_calls2
        


def main():
    #variables
    names = ["Bob", "Mary", "Sue", "John", "Mike", "Becky"]
    calls = [20, 11, 15, 32, 17, 28]
    highest_name = str()
    highest_calls = int()

    highest_name, highest_calls = FindHighest(names, calls)
    print(highest_name, "\t", highest_calls)
main()
