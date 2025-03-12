import sys

while True:
    accept = True
    pwd = sys.stdin.readline().rstrip()
    if pwd == 'end':
        break
    
    vowels = ['a','e','i','o','u']
    cnt_vowel = 0
    for i in range(len(pwd)):
        # 2번 조건 확인
        if pwd[i] in vowels:
            cnt_vowel += 1      # 1번 조건 확인을 위한 모음 카운트
            if i < len(pwd) - 2 and pwd[i+1] in vowels and pwd[i+2] in vowels:
                accept = False
                break
        else:
            if i < len(pwd) - 2 and pwd[i+1] not in vowels and pwd[i+2] not in vowels:
                accept = False
                break
        
        # 3번 조건 확인
        if len(pwd) > 1 and i < len(pwd) - 1 and pwd[i] == pwd[i+1]:
            if pwd[i] != 'e' and pwd[i] != 'o':
                accept = False
                break
    
    # 1번 조건 확인
    if not cnt_vowel:
        accept = False
    
    if not accept:
        print(f"<{pwd}> is not acceptable.")
    else:
        print(f"<{pwd}> is acceptable.")
    