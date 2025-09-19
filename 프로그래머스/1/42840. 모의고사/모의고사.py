def solution(answers):
    answer = []
    students = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == ((i+1) % 5):
            students[0] += 1
        if (i+1) % 5 == 0 and answers[i] == 5:
            students[0] += 1
            
        if (i+1) % 2 == 1 and answers[i] == 2:
            students[1] += 1
        if (i+1) % 8 == 2 and answers[i] == 1:
            students[1] += 1
        if (i+1) % 8 == 4 and answers[i] == 3:
            students[1] += 1
        if (i+1) % 8 == 6 and answers[i] == 4:
            students[1] += 1
        if (i+1) % 8 == 0 and answers[i] == 5:
            students[1] += 1
        
        if ((i+1) % 10 == 1 or (i+1) % 10 == 2) and answers[i] == 3:
            students[2] += 1
        if ((i+1) % 10 == 3 or (i+1) % 10 == 4) and answers[i] == 1:
            students[2] += 1
        if ((i+1) % 10 == 5 or (i+1) % 10 == 6) and answers[i] == 2:
            students[2] += 1
        if ((i+1) % 10 == 7 or (i+1) % 10 == 8) and answers[i] == 4:
            students[2] += 1
        if ((i+1) % 10 == 9 or (i+1) % 10 == 0) and answers[i] == 5:
            students[2] += 1

    answer = list(filter(lambda x: students[x] == max(students), range(len(students))))
    answer = [answer[i]+1 for i in range(len(answer))]
    return answer