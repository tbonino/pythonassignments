#variables
number = int()
size = int()
triangle = str()

#inputs
number = int(input("Number:"))
size = int(input("Size:"))

#outer loop
for number in range (number):
    #inner loop
    for i in range (size):
        print("*" * i, end=" ")
        print(" ")
    #end inner loop
    print(" ")
#end outer loop
