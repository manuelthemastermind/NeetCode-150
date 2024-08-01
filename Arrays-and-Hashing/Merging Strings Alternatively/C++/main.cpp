class Solution
{
public:
     std::string mergeAlternately(std::string word1, std::string word2)
     {
        std::string result = "";

        for(int index = 0; index < word1.length() || index < word2.length(); index++)
        {
            if(index < word1.length())
                result += word1[index];
            if(index < word2.length())
                result += word2[index];
        }

        return result;

     }


};