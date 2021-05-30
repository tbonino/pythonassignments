def HalfList(mynumbers):
    index = int()
    index = 0
    HalfList_sum = int()
    for i in range(0,int(len(mynumbers)/2)):
        HalfList_sum = HalfList_sum + mynumbers[index]
        index = index + 1
    return HalfList_sum

def main():
    mynumbers = [0] * 6
    mytotal = int()

    mynumbers = [6, 5, 7, 9, 4, 3,]
    mytotal = HalfList(mynumbers)
    print(mytotal)

main()
        
