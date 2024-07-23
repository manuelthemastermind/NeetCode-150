#include <iostream>
#include <vector>
#include <unordered_map>

class Solution 
{
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) 
    {
     std::unordered_map <int, int> hashmap;

     for(int i = 0; i < nums.size(); i++)
     {
        int diff = target - nums[i];

        if(hashmap.count(diff))
            return {hashmap[diff], i};
        hashmap[nums[i]] = i;
     }
     return {};   
    }
};
