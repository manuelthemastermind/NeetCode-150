"""
Time-Complexity(O(n^2)), Space Complexity:O(1)
def MissingNumber(nums):
    arrlen = len(nums)+1
    
    for num in range(arrlen):
        if num not in nums:
            return num 

print(MissingNumber([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
"""

"""
Time-Complexity: O(n), Space Complexity: O(n)
def MissingNumber(nums):
    hashset = set(nums)
    arrlen = len(nums) + 1 
    
    for num in range(arrlen):
        if num not in hashset:
            return num 
print(MissingNumber([0,1,2,3,4,5]))
""" 

"""
Time Complexity: O(n), Space Complexity: O(1)
"""

def MissingNumber(nums):
    arrlen = len(nums) 
    missingsum = arrlen * (arrlen + 1) // 2 
    actualsum = sum(nums)
    return missingsum - actualsum

print(MissingNumber([0,1,2,4,5,6]))
    
    
