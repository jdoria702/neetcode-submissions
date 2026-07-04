class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort strings by character in the array using .sort()
        # .sort() is in place function
        # compare the first and last words (most different)
        strs.sort()
        word1 = strs[0]
        word2 = strs[-1]
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return word1[:i]
            
        return min(word1, word2)