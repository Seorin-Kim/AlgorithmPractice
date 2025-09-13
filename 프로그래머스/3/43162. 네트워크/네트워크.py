def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(idx):
        if visited[idx]:
            return False
        
        visited[idx] = 1
        for i, c in enumerate(computers[idx]):
            if i != idx and c and not visited[i]:
                dfs(i)
        
        return True
    
    for i in range(n):
        if dfs(i):
            answer += 1
    
    return answer