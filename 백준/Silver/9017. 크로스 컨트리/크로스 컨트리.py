import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    race = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = dict()
    score = dict()

    for t in race:
        if t in cnt.keys():
            cnt[t] += 1
        else:
            cnt[t] = 1

    fail = 0
    for i in range(n):
        if cnt[race[i]] < 6:
            fail += 1
            continue
        else:
            if race[i] in score.keys():
                score[race[i]].append(i + 1 - fail)
            else:
                score[race[i]] = [i + 1 - fail]
    
    score = sorted(score, key=lambda x:(sum(score[x][:4]), score[x][4]))
    print(score[0])

