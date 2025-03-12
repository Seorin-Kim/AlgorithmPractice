n = int(input())
ppl = []
for i in range(n):
    a = tuple(map(int, input().split()))
    ppl.append(a)

for j in range(n):
    rank = 0
    for k in range(1, n+1):
        if ppl[j][0] < ppl[(j+k) % n][0] and ppl[j][1] < ppl[(j+k) % n][1]:
            rank += 1
    print(rank + 1, end=" ")
