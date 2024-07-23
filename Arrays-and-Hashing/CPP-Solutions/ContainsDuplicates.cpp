#include <iostream>
#include <unordered_set>
#include <vector>

class Solution
{
public: 
      bool containsduplicates(std::vector <int>& nums)
      {
        std::unordered_set <int> hashset;

        for(int i = 0; i < nums.size(); i++)
        {
            if(hashset.find(nums[i]) != hashset.end())
                return true;
            hashset.insert(nums[i]);
        }

        return false;

      }  
};

int main()
{
    Solution solution;

    std::vector <int> Vect = {1,2,3,4};
   std::cout << solution.containsduplicates(Vect);
}