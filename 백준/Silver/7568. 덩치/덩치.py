import sys

n = int(sys.stdin.readline().rstrip())
ppl = []
for i in range(n):
    a = tuple(map(int, sys.stdin.readline().rstrip().split()))
    ppl.append(a)

for i in range(n):
    rank = 1
    for j in range(1, n):
        if ppl[i][0] < ppl[(i+j) % n][0] and ppl[i][1] < ppl[(i+j) % n][1]:
            rank += 1
    print(rank, end=" ")
