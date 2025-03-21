import sys

n, score, p = map(int, sys.stdin.readline().rstrip().split())
rank = 1

if n == 0:
    pass
else:
    ranking_list = list(map(int, sys.stdin.readline().rstrip().split()))

    if n == p and ranking_list[-1] >= score:
        rank = -1
    else:
        for i in range(n):
            if ranking_list[i] > score:
                rank += 1
            elif ranking_list[i] < score:
                break
        
print(rank)
