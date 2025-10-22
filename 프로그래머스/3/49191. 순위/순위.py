def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    for a, b in results:
        win[a].append(b)
        lose[b].append(a)
    
    for i in range(1, n+1):
        visited = [0] * (n+1)

        def dfs(cur, graph):
            visited[cur] = 1
            for nxt in graph[cur]:
                if not visited[nxt]:
                    dfs(nxt, graph)

        dfs(i, win)
        dfs(i, lose)
    
        if sum(visited) == n:
            answer += 1
            
    return answer