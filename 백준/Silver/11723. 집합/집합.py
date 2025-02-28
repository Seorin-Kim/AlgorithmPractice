import sys

n = int(sys.stdin.readline().rstrip())
S = set([])

for _ in range(n):
    cmd = list(sys.stdin.readline().rstrip().split())
    if len(cmd) > 1:
        op, x = cmd[0], int(cmd[1])
    else:
        op = cmd[0]
        
    if op == 'add':
        S.add(x)
    elif op == 'remove':
        if x in S:
            S.remove(x)
    elif op == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif op == 'all':
        S = set([i for i in range(1,21)])
    elif op == 'empty':
        S = set([])
