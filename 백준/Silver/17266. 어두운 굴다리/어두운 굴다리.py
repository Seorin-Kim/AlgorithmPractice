import sys
import math

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
locations = list(map(int, sys.stdin.readline().rstrip().split()))

# 가로등 사이의 거리 저장
diff = []
for i in range(len(locations)-1):
    diff.append(locations[i+1] - locations[i])

diff = [math.ceil(i/2) for i in diff]
diff.append(locations[0])       # 맨 앞 가로등
diff.append(n-locations[-1])    # 맨 뒤 가로등

print(max(diff))
