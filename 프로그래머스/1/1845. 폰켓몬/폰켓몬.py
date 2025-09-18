def solution(nums):
    hash = {}
    for n in nums:
        if n not in hash.keys():
            hash[n] = 1
        else:
            hash[n] += 1

    hash_keys = list(hash.keys())
    if len(hash_keys) >= len(nums) / 2:
        return len(nums) / 2
    else:
        return len(hash_keys)
