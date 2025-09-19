def solution(n, lost, reserve):
    students = [1] * n
    for i in lost:
        students[i-1] -= 1
    for i in reserve:
        students[i-1] += 1
    
    for i in range(len(students)):
        if students[i] == 0:
            if i - 1 >= 0 and students[i - 1] == 2:
                students[i - 1] -= 1
                students[i] += 1
            elif i + 1 < n and students[i + 1] == 2:
                students[i + 1] -= 1
                students[i] += 1
    
    cnt = [1 for i in students if i > 0]
    return sum(cnt)