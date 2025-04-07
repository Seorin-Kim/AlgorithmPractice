import sys
import math

n = int(sys.stdin.readline().rstrip())
num_candidate = list(map(int, sys.stdin.readline().rstrip().split()))
b, c = map(int, sys.stdin.readline().rstrip().split())

num_supervisor = 0
for i in range(n):
    if num_candidate[i] >= b:
        num_supervisor += 1
        num_supervisor += math.ceil((num_candidate[i] - b) / c)
    else:
        num_supervisor += 1

print(num_supervisor)
