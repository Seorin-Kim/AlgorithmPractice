import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    input = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(input)

max_val = max(map(max, board))
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(cnt, tmp_sum, trace):
    global sum_

    if tmp_sum + (4-cnt) * max_val < sum_:
        return
    
    if cnt == 4:
        if tmp_sum > sum_:
            sum_ = tmp_sum
        return
    
    for (cur_x, cur_y) in trace:
        for dir in range(4):
            next_x = cur_x + dx[dir]
            next_y = cur_y + dy[dir]
            if 0 <= next_x < n and 0 <= next_y < m and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                dfs(cnt+1, tmp_sum+board[next_x][next_y], trace+[(next_x, next_y)])
                visited[next_x][next_y] = 0

sum_ = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(1, board[i][j], [(i, j)])
        visited[i][j] = 0

print(sum_)
