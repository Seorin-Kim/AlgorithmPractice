def solution(n, q, ans):
    from itertools import combinations
    
    answer = []
    for comb in combinations(range(1, n+1), 5):
        flag = True
        for i in range(len(q)):
            cnt = 0
            for num in q[i]:
                if num in comb:
                    cnt += 1
            if cnt != ans[i]:
                flag = False
                break
        if flag:
            answer.append(comb)
    
    return len(answer)