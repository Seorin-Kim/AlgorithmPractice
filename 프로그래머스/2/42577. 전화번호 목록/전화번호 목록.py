def solution(phone_book):
    idx_dict = {}
    for num in phone_book:
        idx = int(num[0])
        if idx not in idx_dict.keys():
            idx_dict[idx] = []
        idx_dict[idx].append(num)
    
    for idx in idx_dict.keys():
        if len(idx_dict[idx]) > 1:
            idx_dict[idx].sort()
            for i in range(len(idx_dict[idx]) - 1):
                if idx_dict[idx][i+1].startswith(idx_dict[idx][i]):
                    return False

    return True