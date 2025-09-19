def solution(brown, yellow):
    ans = 0
    tmp = brown // 2
    for i in range(2, tmp-1):
        if (i - 1) * (tmp-i -1) == yellow:
            ans = i
            break
            
    answer = [ans + 1, tmp-ans + 1]
    if answer[0] < answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
        
    return answer