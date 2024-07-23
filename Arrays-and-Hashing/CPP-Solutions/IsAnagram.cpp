#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

class Solution
{
public:
    bool isAnagram(std::string s, std::string t)
    {
        if(s.size() != t.size())
            return false;
        std::vector <int> alphabetVect(26,0); //Holds the alphabet

        for(int i = 0; i < s.size(); i++)
        {
            alphabetVect[s[i] - 'a']++;
            alphabetVect[t[i] - 'a']--;
        }

        for(int i = 0; i < 26; i++)
        {
            if(alphabetVect[i] != 0)
                return false;
        }
        return true;
    }

};

