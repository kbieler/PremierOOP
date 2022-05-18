#Given an array/list [] of integers , Find the product of the k maximal numbers.
Ex1 = [10,3,-27,-1] 
#3
#Output => -30
Ex2 = [14,29,-28,39,-16,-48]
#4
#Output => -253344


import math

##nums = sorted(Ex1)
#print(nums)
#tops = nums[-3:]
#print(tops)

def product(arr, k):
    nums = sorted(arr)
    tops = nums[-k:]
    pro = math.prod(tops)
    return pro
   

print(product(Ex2, 4))