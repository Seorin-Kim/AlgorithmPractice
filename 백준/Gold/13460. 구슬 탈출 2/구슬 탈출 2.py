import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

red = [-1, -1]
blue = [-1, -1]
hole = [-1, -1]
board = [[1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    input = sys.stdin.readline().rstrip()
    for j in range(m):
        if input[j] == '#':
            board[i][j] = 0
        elif input[j] == 'B':
            blue = [i, j]
        elif input[j] == 'R':
            red = [i, j]
        elif input[j] == 'O':
            hole = [i, j]

q = deque()
q.append((red, blue, 0))
visited = set()
visited.add((red[0], red[1], blue[0], blue[1]))

directions = ['up', 'down', 'left', 'right']
success = False
while q:
    r, b, cnt = q.popleft()
    if r == hole:
        success = True
        print(cnt)
        break
    if cnt > 10:
        break
    
    # 4방향 순서대로 시도
    for dir in directions:
        if dir == 'up':
            drow, dcol = -1, 0
        elif dir == 'down':
            drow, dcol = 1, 0
        elif dir == 'left':
            drow, dcol = 0, -1
        else:
            drow, dcol = 0, 1

        # red 움직이기
        r_move = 0
        r_tmp = r.copy()
        while True:
            r_tmp[0] += drow
            r_tmp[1] += dcol
            r_move += 1
            if board[r_tmp[0]][r_tmp[1]] == 0:
                r_tmp[0] -= drow
                r_tmp[1] -= dcol
                break
            elif r_tmp == hole:
                break

        # blue 움직이기
        b_move = 0
        b_tmp = b.copy()
        while True:
            b_tmp[0] += drow
            b_tmp[1] += dcol
            b_move += 1
            if board[b_tmp[0]][b_tmp[1]] == 0:
                b_tmp[0] -= drow
                b_tmp[1] -= dcol
                break
            elif b_tmp == hole:
                break

        # blue가 구멍에 빠지면 해당 방향은 없던 일로
        if b_tmp == hole:
            continue

        # red, blue가 같은 칸에서 멈추면, 더 많이 움직인 공을 한 칸 덜 오도록 밀어야 함
        if r_tmp == b_tmp:
            if r_move > b_move:
                r_tmp[0] -= drow
                r_tmp[1] -= dcol
            else:
                b_tmp[0] -= drow
                b_tmp[1] -= dcol

        if (r_tmp[0], r_tmp[1], b_tmp[0], b_tmp[1]) not in visited:
            visited.add((r_tmp[0], r_tmp[1], b_tmp[0], b_tmp[1]))
            q.append((r_tmp, b_tmp, cnt+1))

if not success:
    print(-1)
