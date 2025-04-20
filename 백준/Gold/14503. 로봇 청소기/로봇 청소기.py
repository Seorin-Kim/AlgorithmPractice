import sys

n, m = map(int, sys.stdin.readline().rstrip().rsplit())
# 0: 북, 1: 동, 2: 남, 3: 서
r, c, d = map(int, sys.stdin.readline().rstrip().rsplit())
board = []
for _ in range(n):
    input = list(map(int, sys.stdin.readline().rstrip().rsplit()))
    board.append(input)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1
    
    if 0 <= r-1 < n and 0 <= r+1 < n and 0 <= c-1 < m and 0 <= c+1 < m:
        if board[r-1][c] != 0 and board[r+1][c] != 0 and board[r][c-1] != 0 and board[r][c+1] != 0:
            if board[r-dx[d]][c-dy[d]] != 1:
                r -= dx[d]
                c -= dy[d]
                continue
            else:
                print(cnt)
                break
        else:
            d = (d - 1) % 4
            if board[r+dx[d]][c+dy[d]] == 0:
                r += dx[d]
                c += dy[d]
                continue
