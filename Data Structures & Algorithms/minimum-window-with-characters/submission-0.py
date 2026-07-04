class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the smallest substring of s, such that all letters of t are in s

        Maintain count of both strings for the required characters in string t
        Subsequence of s is valid if it contains all characters in t hashmap
        """

        s_count = {}
        t_count = {}

        have = 0
        need = 0

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        need = len(t_count)
        
        l = 0
        r = 0
        shortest = (0, 10000)
        while r < len(s):
            if s[r] in t_count:
                # Increment a needed character count
                s_count[s[r]] = s_count.get(s[r], 0) + 1

                # Character found, fulfills a need in t_count
                if s_count.get(s[r]) == t_count.get(s[r]):
                    have = have + 1

                    # Record size of window and move left pointer forward
                    while have == need:
                        if r - l + 1 < shortest[1] - shortest[0] + 1:
                            shortest = (l, r)
                        
                        if s[l] in s_count:
                            s_count[s[l]] = s_count[s[l]] - 1
                            if s_count[s[l]] < t_count[s[l]]:
                                have = have - 1
                        
                        l = l + 1
                
            r = r + 1

        if shortest == (0, 10000):
            return ""
        return s[shortest[0]:shortest[1]+1]