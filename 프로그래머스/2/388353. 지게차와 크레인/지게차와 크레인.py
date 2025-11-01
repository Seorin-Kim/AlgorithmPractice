def solution(storage, requests):
    from collections import deque

    board = []
    board.append(['#'] * (len(storage[0]) + 2))
    for s in storage:
        board.append(['#'] + list(s) + ['#'])
    board.append(['#'] * (len(storage[0]) + 2))
    

    def find_edges():
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        edges = set()
        q = deque()
        visited = set()

        q.append((0, 0))
        visited.add((0, 0))
        while q:
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in visited:
                    if board[nx][ny] == '#':
                        visited.add((nx, ny))
                        q.append((nx, ny))
                    else:
                        edges.add((nx, ny))
        
        return edges

    
    
    for req in requests:
        if len(req) == 1:   # 지게차
            edges = find_edges()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == req[0] and (i, j) in edges:
                        board[i][j] = '#'
            
        else:               # 크레인
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == req[0]:
                        board[i][j] = '#'    
        
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '#':
                cnt += 1
                
    return cnt