import sys

input = list(map(int, sys.stdin.readline().rstrip().split()))
n, k = input[0], input[1]
results = [[0,0,0,0] for _ in range(n)]

for i in range(n):
    input = list(map(int, sys.stdin.readline().rstrip().split()))
    idx, gold, silver, bronze = input[0], input[1], input[2], input[3]
    results[i] = [idx, gold, silver, bronze]

results.sort(key=lambda x: (x[1], x[2], x[3]))

rank = 0
for i in range(n):
    if i > 0 and results[i][1] == results[i-1][1] and results[i][2] == results[i-1][2] and results[i][3] == results[i-1][3]:
        pass
    else:
        rank += 1
    
    if results[i][0] == k:
        break
    
print(rank)
