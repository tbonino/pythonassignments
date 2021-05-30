
# Get our input from the command line
import sys
numbers = [1,2,3,4,5,6,7,8,9]
for i in range(0,len(numbers)):
  numbers[i]= int(numbers[i])

def isEven(n) :
  return ((n % 2) == 0)

# Your code goes here

def main():
  odd = []
  even = []
  num = float()
  for i in range(0,len(numbers)):
    num = isEven(numbers[i])
    if num != 0:
      even.append(numbers[i])
    else:
      odd.append(numbers[i])
  print(odd)
  print(even)

main()
