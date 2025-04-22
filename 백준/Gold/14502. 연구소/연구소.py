import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().rsplit())
board = []
viruses = []
empties = []
for i in range(n):
    input = list(map(int, sys.stdin.readline().rstrip().rsplit()))
    for j in range(m):
        if input[j] == 2:
            viruses.append((i, j))
        if input[j] == 0:
            empties.append((i, j))
    board.append(input)

wall_combination = set()
def combination(arr, r):
    def generate(chosen):
        if len(chosen) == r:
            wall_combination.add(tuple(chosen.copy()))
            return

        if chosen:
            start = arr.index(chosen[-1]) + 1
        else:
            start = 0
        
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
combination(empties, 3)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_cnt = 0
for walls in wall_combination:
    tmp_board = [board[i].copy() for i in range(len(board))]
    for (i, j) in walls:
        tmp_board[i][j] = 1

    q = deque(viruses)
    while q:
        cur_x, cur_y = q.popleft()
        for dir in range(4):
            next_x = cur_x + dx[dir]
            next_y = cur_y + dy[dir]
            if 0 <= next_x < n and 0 <= next_y < m and tmp_board[next_x][next_y] == 0:
                tmp_board[next_x][next_y] = 2
                q.append((next_x, next_y))
    
    cnt = sum([empty.count(0) for empty in tmp_board])
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
