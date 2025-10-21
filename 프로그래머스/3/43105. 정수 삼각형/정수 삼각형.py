def solution(triangle):
    answer = []
    
    for i in range(len(triangle)):
        answer.append([])
        if i == 0:
            answer[i].append(triangle[0][0])
            continue
            
        for k in range(i+1):
            if k == 0:
                answer[i].append(answer[i-1][0] + triangle[i][0])
            elif k == i:
                answer[i].append(answer[i-1][-1] + triangle[i][-1])
            else:
                answer[i].append(max(answer[i-1][k-1], answer[i-1][k]) + triangle[i][k])
        
    return max(answer[-1])