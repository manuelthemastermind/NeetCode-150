class Solution {
public:
    int romanToInt(std::string s) 
    {
        std::unordered_map <char, int> hashmap;

        hashmap['I'] = 1;
        hashmap['V'] = 5;
        hashmap['X'] = 10;
        hashmap['L'] = 50;
        hashmap['C'] = 100;
        hashmap['D'] = 500;
        hashmap['M'] = 1000;

        int result = 0;

        for(int i = 0; i < s.length(); i++)
        {
            if(hashmap[s[i]] < hashmap[s[i+1]])
                result -= hashmap[s[i]];
            else
                result += hashmap[s[i]];
        }

        return result;
    }
};