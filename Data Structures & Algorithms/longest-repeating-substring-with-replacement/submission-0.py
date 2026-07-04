class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding window

        Use hash map to track frequency of characters

        Window constraint:
            - length of window - highest_frequency <= k
        
        Slide left pointer and decrement frequencies until constraint is met
        """

        count = {}
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            
            most_frequent = max(count.values())
            if (r - l + 1) - most_frequent <= k:
                longest = max(longest, r - l + 1)
            else:
                while (r - l + 1) - most_frequent > k:
                    count[s[l]] = count[s[l]] - 1
                    most_frequent = max(count.values())
                    l = l + 1

            r = r + 1

        return longest