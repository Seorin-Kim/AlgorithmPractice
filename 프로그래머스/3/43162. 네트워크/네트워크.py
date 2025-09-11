def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(idx):
        if visited[idx]:
            return
        visited[idx] = 1
        for i, c in enumerate(computers[idx]):
            if not visited[i] and c:
                dfs(i)
        return True
    
    for i in range(n):
        if dfs(i):
            answer += 1
    
    return answer