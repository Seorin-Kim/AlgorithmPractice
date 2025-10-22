def solution(n, edge):
    from collections import deque
    
    graph = [[] for _ in range(n)]
    for v1, v2 in edge:
        graph[v1-1].append(v2-1)
        graph[v2-1].append(v1-1)
        
    visited = [0] * n
    
    def bfs(begin):
        q = deque()
        q.append(begin)
        visited[begin] = 1
        
        while q:
            v = q.popleft()
            for nv in graph[v]:
                if visited[nv] == 0:
                    visited[nv] = visited[v] + 1
                    q.append(nv)
        
    bfs(0)
    
    return visited.count(max(visited))