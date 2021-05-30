# Get our numbers from the command line
import sys
numbers= sys.argv[1].split(',')
numbers= [int(i) for i in numbers]

# Your code goes here
index = int()
highest_number = int()
integer = int()
result = int()
highest_number = numbers[0]
index = 0

for index in range(0, len(numbers)):
  integer = numbers[index]
  if integer > highest_number:
    highest_number = integer
    result = index
print(result)
