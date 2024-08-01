class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {
        unordered_set <int> hashset;

        for(int i = 0; i < nums.size(); i++)
        {
            if(hashset.find(nums[i]) != hashset.end())
                return true;
            hashset.insert(nums[i]);
        }

        return false;
    }
};
