def solution(schedules, timelogs, startday):
    answer = 0
    
    for sch, tlog in zip(schedules, timelogs):
        if sch % 100 < 50:
            safe = sch + 10
        else:
            safe = sch + 100 - 50
            
        flag = True
        for i in range(7):
            day = (i + startday) % 7
            if day == 6 or day == 0:
                continue
            if tlog[i] > safe:
                flag = False
                break
        if flag:
            answer += 1
    
    return answer