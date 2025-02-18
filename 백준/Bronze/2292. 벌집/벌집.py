# 1: 1          (1)
# 2: 2 - 7      (6 =6*1)
# 3: 8 - 19     (12=6*2)
# 4: 20 - 37    (18=6*3)
# 5: 38 - 61    (24=6*4)

# n = 1 + 6 * (0+1+2+3+4+...)

n = int(input())
sum = 1
num_layers = 1

while n > sum:
    sum = sum + 6 * num_layers
    num_layers += 1

print(num_layers)