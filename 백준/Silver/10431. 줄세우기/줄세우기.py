import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    input = list(map(int, sys.stdin.readline().rstrip().split()))
    t = input[0]
    input.pop(0)

    line = []
    cnt = 0
    # input에서 한 명씩 데려와서 line에 줄 세울 것 
    for i in range(20):
        # line이 비워져 있거나 input[i]가 가장 크다면, 뒤에 줄 세우기만 하면 됨
        if len(line) == 0 or line[-1] < input[i]:
            line.append(input[i])

        # 그게 아니라면, 넣어서 sort 시키고 index 찾아서 뒤에 이동한 인원 세어보면 됨
        else:
            line.append(input[i])
            line.sort()
            idx = line.index(input[i])
            cnt += len(line) - (idx + 1)
    
    print(t, cnt)


