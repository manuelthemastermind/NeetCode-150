class Solution {
public:
    int findClosestNumber(std::vector<int>& nums) 
    {
        int closest = nums[0];

        for(int num : nums)
        {
            if(abs(num) < abs(closest))
                closest = num;
            if(abs(num) == abs(closest))
                closest = std::max(closest, num);
        }
        return closest;
    }
};