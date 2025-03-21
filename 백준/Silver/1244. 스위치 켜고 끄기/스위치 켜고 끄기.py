import sys

num_switch = int(sys.stdin.readline().rstrip())
switches = list(map(int, sys.stdin.readline().rstrip().split()))
num_student = int(sys.stdin.readline().rstrip())
students = []
for _ in range(num_student):
    input = list(map(int, sys.stdin.readline().rstrip().split()))
    students.append(input)


for i in range(num_student):
    if students[i][0] == 1: # 남학생
        n = students[i][1]
        while n <= num_switch:
            if switches[n-1] == 0:
                switches[n-1] = 1
            else:
                switches[n-1] = 0
            n += students[i][1]
    else:                   # 여학생
        n = students[i][1]
        if switches[n-1] == 0:
            switches[n-1] = 1
        else:
            switches[n-1] = 0

        for j in range(1, num_switch):
            if n-1-j < 0 or n-1+j > num_switch - 1:
                break
            else:
                if switches[n-1-j] != switches[n-1+j]:
                    break
                else:
                    if switches[n-1-j] == 0:
                        switches[n-1-j] = 1
                        switches[n-1+j] = 1
                    else:
                        switches[n-1-j] = 0
                        switches[n-1+j] = 0

for i in range(num_switch):
    print(switches[i], end=" ")
    if i % 20 == 19:
        print()
