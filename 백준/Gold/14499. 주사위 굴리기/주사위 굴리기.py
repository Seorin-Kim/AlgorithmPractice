import sys

n, m, x, y, k = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    input = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(input)
# 1: 동, 2: 서, 3: 북, 4: 남
moves = list(map(int, sys.stdin.readline().rstrip().split()))
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

cur = [x, y]
dice = [[0 for _ in range(3)] for _ in range(4)]
for move in moves:
    # 이동한 위치가 지도 밖이면 무시
    if cur[0]+dx[move] < 0 or cur[0]+dx[move] >= n or cur[1]+dy[move] < 0 or cur[1]+dy[move] >= m:
        continue

    # 주사위 위치 이동
    cur[0] += dx[move]
    cur[1] += dy[move]

    # 주사위 정보 수정
    if move == 1:
        tmp1 = dice[1]
        tmp2 = dice[3][1]
        dice[1] = [tmp2, tmp1[0], tmp1[1]]
        dice[3][1] = tmp1[2]
    elif move == 2:
        tmp1 = dice[1]
        tmp2 = dice[3][1]
        dice[1] = [tmp1[1], tmp1[2], tmp2]
        dice[3][1] = tmp1[0]
    elif move == 3:
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = tmp
    else:
        tmp = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i-1][1]
        dice[0][1] = tmp

    # 규칙에 따라 바닥면 수정
    if board[cur[0]][cur[1]] == 0:
        board[cur[0]][cur[1]] = dice[3][1]
    else:
        dice[3][1] = board[cur[0]][cur[1]]
        board[cur[0]][cur[1]] = 0
    
    # 윗면 출력
    print(dice[1][1])
