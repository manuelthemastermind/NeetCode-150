""""
O(n^2) Complexity
"""
def containsDuplicate(nums):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    return True
        return False
            
print(containsDuplicate([5,6,7,8,9]))
        