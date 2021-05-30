# Get our list from the command line
import sys
numbers = sys.argv[1].split(",")

# Your code goes here
total = int ()
total = 0

for i in range(0,len(numbers)):
  numbers[i] = int(numbers[i])
  total = total + numbers[i]

print(total)
