def FindMin(my_numbers):
    index = int()
    minimum = int()
    search = int()
    position = int()
    minimum = my_numbers[0]
    for index in range(0,len(my_numbers)):
        search = my_numbers[index]
        if search < minimum:
            minimum = search
            position = index
    return minimum, position
    
def main():
    #variables
    my_numbers = [22, 46, 78, 15, 98, 101]
    smallest_int = int()
    smallest_index = int()
    smallest_int, smallest_index = FindMin(my_numbers)

    print(smallest_int, "\t", smallest_index)
main()
