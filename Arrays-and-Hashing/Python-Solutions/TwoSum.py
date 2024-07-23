
""""
Naive Approach: O(n^2) Time Complexity

def TwoSum(nums, target):
    arrlength = len(nums) 
    for i in range(arrlength):
        for j in range(i+1, arrlength):
            if(nums[i] + nums[j] == target):
                return [i,j]
"""
def TwoSum(nums, target):
        hashmap = {}  # Initialize an empty hashmap to store value:index pairs

        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in hashmap):
                return [hashmap[diff], i]
            hashmap[nums[i]] = i;
        return

        # return  # If no pair is found, implicitly return None (can be changed to `return []`)

print(TwoSum([0,1,2,3,4,5,20], 25))


