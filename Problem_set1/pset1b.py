###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Thang Tran
# Collaborators: Thang Tran
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    import math
    egg_order= list(egg_weights)
    egg_order.reverse() 
    count=0
    for i in egg_order:
        memo[i] = math.floor(target_weight/i)
        target_weight=target_weight%i
    
    for i in memo.values(): 
        count +=i
    return count, memo

egg_weights = (1, 5, 10, 25)
n = 99
print("Egg weights: ", egg_weights)
print("target n=", n)
print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
print("Actual output:", dp_make_weight(egg_weights, n))
print() 
