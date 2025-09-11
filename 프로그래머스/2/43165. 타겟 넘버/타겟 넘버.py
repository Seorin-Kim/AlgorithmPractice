def solution(numbers, target):
    answer = 0
    
    def dfs(idx, sum):
        if idx == len(numbers):
            if sum == target:
                nonlocal answer
                answer += 1
        else:
            dfs(idx + 1, sum + numbers[idx])
            dfs(idx + 1, sum - numbers[idx])
    
    dfs(0, 0)
    
    return answer