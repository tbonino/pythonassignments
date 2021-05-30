def ValidatePassword(myword, mycharacter):
    index = int()
    validate = bool
    search = str()
    index = 0
    validate = False
    while validate == False and index < len(myword):
        search = myword[index]
        if search == mycharacter:
            validate = True
        else:
            index = index + 1
            validate = False
    return validate

def main():
     myword = ["" * 9]
     mycharacter = str()
     myfound = bool()

     myword = ["P", "a", "s", "s", "&", "W", "o", "r", "d"]
     mycharacter = "g"
     myfound = ValidatePassword(myword, mycharacter)
     print(myfound)
main()
