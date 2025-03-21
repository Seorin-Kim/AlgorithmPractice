import sys

n = int(sys.stdin.readline().rstrip())

heart = (-1, -1)
body = [-1, -1, -1, -1, -1]
waist = 0
left_leg = 1
right_leg = 1

for i in range(n):
    row = sys.stdin.readline().rstrip()
    if '*' in row:
        if heart[0] < 0:    # 심장 위치 지정
            heart = (i + 2, row.index('*') + 1)
        elif body[0] < 0:   # 팔 길이 저장
            left = row.index('*')
            right = row.rindex('*')
            body[0] = heart[1] - left - 1
            body[1] = right - heart[1] + 1
        elif body[2] < 0:   # 허리 길이 측정하다가, 다리가 시작되면 허리길이 저장
            if row.index('*') == row.rindex('*'):
                waist += 1
            else:           # 다리 시작되는 행에서 들어가는 조건문
                body[2] = waist
        else:
            if row.index('*') != row.rindex('*'):
                left_leg += 1
                right_leg += 1
            elif row.index('*') < heart[1] - 1:
                left_leg += 1
            elif row.index('*') > heart[1] - 1:
                right_leg += 1
    body[3] = left_leg
    body[4] = right_leg

print(heart[0], heart[1])
for i in range(5):
    print(body[i], end=" ")
