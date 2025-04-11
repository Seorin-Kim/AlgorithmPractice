import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
t_list = []
p_list = []
for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    t_list.append(t)
    p_list.append(p)

total = [0 for _ in range(n+1)]
for i in range(n-1, -1, -1):
    if i + t_list[i] <= n and p_list[i] + total[i+t_list[i]] > total[i+1]:
        total[i] = p_list[i] + total[i+t_list[i]]
    else:
        total[i] = total[i+1]

print(total[0])
