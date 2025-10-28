def solution(dice):
    from itertools import combinations, product
    from bisect import bisect_left
    
    dice_combs = list(combinations(range(len(dice)), len(dice)//2))
    max_cnt = 0
    for dice_comb in dice_combs:
        a_dice = [dice[i] for i in dice_comb]
        b_dice = list(filter(lambda x: x not in a_dice, dice))
        
        a_score = [sum(nums) for nums in product(*a_dice)]
        b_score = [sum(nums) for nums in product(*b_dice)]
        b_score.sort()
        
        cnt = 0
        for a in a_score:
            cnt += bisect_left(b_score, a)
    
            if cnt > max_cnt:
                max_cnt = cnt
                result = [d+1 for d in dice_comb]
                
    return result