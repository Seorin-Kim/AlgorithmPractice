import sys

n = int(sys.stdin.readline().rstrip())

k = int(sys.stdin.readline().rstrip())
apples = []
for _ in range(k):
    loc = list(map(int, sys.stdin.readline().rstrip().split()))
    apples.append(loc)

l = int(sys.stdin.readline().rstrip())
turns = []
for _ in range(l):
    input = list(sys.stdin.readline().rstrip().split())
    turns.append([int(input[0]), input[1]])


sec = 1
direction = 0     # 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
head = [1, 1]
body = [[1, 1]]   # 리스트에 tail -> head 순으로 저장됨
turns_idx = 0

while True:
    if turns_idx >= l or sec <= turns[turns_idx][0]:
        if direction == 0:
            head[1] += 1
        elif direction == 1:
            head[0] += 1
        elif direction == 2:
            head[1] -= 1
        else:
            head[0] -= 1
        
        # 머리가 벽이나 몸에 닿으면 while 탈출
        if head[0] > n or head[0] < 1 or head[1] > n or head[1] < 1 or head in body:
            break
        
        body.append(head.copy())    # body에 head를 추가하고
        if head in apples:          # head 위치에 사과가 있으면 먹기
            apples.remove(head)
        else:                       # 사과 없으면 꼬리 당겨오기
            body.pop(0)
        
        sec += 1
    
    # 방향 바꿔야 할 때
    else:
        if turns[turns_idx][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        turns_idx += 1        
    
print(sec)
