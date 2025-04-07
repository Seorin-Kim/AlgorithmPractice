import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

red = [-1, -1]
blue = [-1, -1]
hole = [-1, -1]
board = []
for i in range(n):
    input = sys.stdin.readline().rstrip()
    board.append(input)
    for j in range(m):
        if input[j] == 'B':
            blue = [i, j]
        elif input[j] == 'R':
            red = [i, j]
        elif input[j] == 'O':
            hole = [i, j]

# 상(0), 하(1), 좌(2), 우(3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((red[0], red[1], blue[0], blue[1], 0))
visited = set()
visited.add((red[0], red[1], blue[0], blue[1]))

success = False
while q:
    rx, ry, bx, by, cnt = q.popleft()
    if board[rx][ry] == 'O':
        success = True
        print(cnt)
        break
    if cnt > 10:
        break
    
    # 상하좌우 순서대로 시도
    for k in range(4):
        # red 움직이기
        rx_move = rx + dx[k]
        ry_move = ry + dy[k]
        r_move = 1
        while True:
            if board[rx_move][ry_move] == '#':
                rx_move -= dx[k]
                ry_move -= dy[k]
                break
            elif board[rx_move][ry_move] == 'O':
                break
            rx_move += dx[k]
            ry_move += dy[k]
            r_move += 1
        
        # blue 움직이기
        bx_move = bx + dx[k]
        by_move = by + dy[k]
        b_move = 1
        while True:
            if board[bx_move][by_move] == '#':
                bx_move -= dx[k]
                by_move -= dy[k]
                break
            elif board[bx_move][by_move] == 'O':
                break
            bx_move += dx[k]
            by_move += dy[k]
            b_move += 1

        # blue가 구멍에 빠지면 해당 방향(상하좌우)은 없던 일로
        if board[bx_move][by_move] == 'O':
            continue

        # red, blue가 같은 칸에서 멈추면, 더 많이 움직인 공을 한 칸 덜 오도록 밀어야 함
        if rx_move == bx_move and ry_move == by_move:
            if r_move > b_move:
                rx_move -= dx[k]
                ry_move -= dy[k]
            else:
                bx_move -= dx[k]
                by_move -= dy[k]

        if (rx_move, ry_move, bx_move, by_move) not in visited:
            visited.add((rx_move, ry_move, bx_move, by_move))
            q.append((rx_move, ry_move, bx_move, by_move, cnt+1))

if not success:
    print(-1)
