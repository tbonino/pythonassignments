def FindToys(toys,search_item):
    index = int()
    found = bool
    search = str()
    index = 0
    found = False
    while found == False and index < len(toys):
        search = toys[index]
        if search == search_item:
            found = True
        else:
            index = index + 1
            found = False
    return found

def main():
    toys = ["ball", "doll", "bat", "puzzle", "legos", "Barbie", "truck"]
    search_item = "bat"
    found_item = bool
    #call search function
    found_item = FindToys(toys, search_item) 
    print(found_item)
main()
