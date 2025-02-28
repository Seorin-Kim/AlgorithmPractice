import sys

n = int(sys.stdin.readline().rstrip())
ch = []
for _ in range(n):
    ch.append(sys.stdin.readline().rstrip())

idx_kbs1 = ch.index('KBS1')
print('1' * idx_kbs1 + '4' * idx_kbs1, end='')
ch.remove('KBS1')
ch.insert(0, 'KBS1')

idx_kbs2 = ch.index('KBS2')
print('1' * idx_kbs2 + '4' * (idx_kbs2-1))