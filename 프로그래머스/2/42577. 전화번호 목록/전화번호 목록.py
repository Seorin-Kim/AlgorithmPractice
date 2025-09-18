def solution(phone_book):
    hash = {}
    phone_book.sort()
    for nums in phone_book:
        if nums[0] not in hash.keys():
            hash[nums[0]] = [nums]
        else:
            hash[nums[0]].append(nums)
    
    for k, v in hash.items():
        if len(v) > 1:
            for i in range(len(v)-1):
                if v[i+1].startswith(v[i]):
                    return False
    
    return True
    