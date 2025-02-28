import sys

word = list(sys.stdin.readline().rstrip().upper())
alpha = {}

for i in word:
    if i in alpha.keys():
        alpha[i] += 1
    else:
        alpha[i] = 1

keys = list(alpha.keys())
nums = list(alpha.values())
max_num = max(nums)
if nums.count(max_num) > 1:
    print("?")
else:
    print(keys[nums.index(max_num)])
