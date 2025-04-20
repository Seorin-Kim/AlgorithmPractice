import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
# 0: 덧셈(+), 1: 뺄셈(-), 2: 곱셈(x), 3: 나눗셈(/)
operations = list(map(int, sys.stdin.readline().rstrip().split()))
operations = [0] * operations[0] + [1] * operations[1] + [2] * operations[2] + [3] * operations[3]

ops_permutation = set()
def permutation(arr, r):
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r:
            ops_permutation.add(tuple(chosen.copy()))
            return
        
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    
    generate([], used)
permutation(operations, n-1)

max_val = -1000000000
min_val = 1000000000
for ops in ops_permutation:
    val = nums[0]
    for i in range(1, n):
        op = ops[i-1]
        if op == 0:
            val += nums[i]
        elif op == 1:
            val -= nums[i]
        elif op == 2:
            val *= nums[i]
        else:
            if val >= 0:
                val = val // nums[i]
            else:
                val = -(-val // nums[i])
    if val > max_val:
        max_val = val
    if val < min_val:
        min_val = val

print(max_val)
print(min_val)
