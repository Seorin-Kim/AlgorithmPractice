def solution(maps):
    from collections import deque
    
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def bfs(x, y):
        q = deque()
        q.append([x, y])
        visited[x][y] = 1
        
        while q:
            x, y = q.popleft()
            if x == n-1 and y == m-1:
                return visited[x][y]

            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])

        return -1
    
    answer = bfs(0, 0)
    
    return answer