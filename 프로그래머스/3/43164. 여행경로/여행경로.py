def solution(tickets):
    answer = []
    tickets.sort()
    visited = [0] * len(tickets)
    
    def dfs(path):
        if len(path) == len(tickets) + 1:
            answer.append(path[:])
            return
        
        for i, [dep, arr] in enumerate(tickets):
            if dep == path[-1] and not visited[i]:
                visited[i] = 1
                path.append(arr)
                dfs(path)
                path.pop()
                visited[i] = 0
    
    dfs(['ICN'])
    answer = answer[0]
    
    return answer