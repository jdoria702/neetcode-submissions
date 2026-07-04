class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window

        Window constraint:
            - All values within the window must not have a repeating character
            - The character encountered must not be in set
        
        If window fails constraint:
            - record length of window
            - update largest size of the window
        """

        l = 0
        r = 0
        distinct = set()
        longest = 0
        while r < len(s):
            if s[r] in distinct:
                longest = max(longest, r - l)

                while s[l] != s[r]:
                    distinct.remove(s[l])
                    l = l + 1
                l = l + 1
                r = r + 1

            else:
                distinct.add(s[r])
                r = r + 1
        
        longest = max(longest, r - l)

        return longest