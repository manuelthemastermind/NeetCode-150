class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        index = 0
        
        while(index < len(word1) or index < len(word2)):
            if(index < len(word1)):
                result += word1[index]
            if(index < len(word2)):
                result += word2[index]
            index += 1
        return result
        