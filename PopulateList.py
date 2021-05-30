# Get N from the command line
import sys
N= int(sys.argv[1])

# Your code goes here
nlist = [0 for i in range(N)]
index = int()
index = 0

for i in range(0, N):
  nlist[index] = index * 10
  index = index + 1

print(nlist)
