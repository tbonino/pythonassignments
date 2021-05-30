#function
def Draw (char, val):
    #draw loop
    for val in range(val + 1):
        print(char * val, end=(""))
        print()
    return result #adding the 'return result' will prevent 'None' being printed on the end
    #end loop
#end function

#global variables
character = str()
size = int()
result = str()

#inputs
character = str(input())
size = int(input())

#call
result = Draw(character, size)

#output
print(result)
