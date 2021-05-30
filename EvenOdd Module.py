#Write your function here
def EvenOdd (integer):
  remainder = int()
  remainder = integer % 2
  if remainder > 0:
    return 'ODD'
  else:
    return 'EVEN'

#Declare the variables you will need in order to call your function and print out the correct value.
#Variables
result = str()
integer = int()

#Get the input from the user.  
integer = int(input())

#Call your function
result = EvenOdd(integer)

#Print out the result returned from your function.
print(result)
