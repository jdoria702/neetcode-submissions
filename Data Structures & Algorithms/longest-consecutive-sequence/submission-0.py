class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        s = list(dict.fromkeys(sorted_nums))
        
        if not s:
            return 0

        if len(s) == 1:
            return 1
        
        longest = 1
        l = 0
        r = 1
        print(s)
        while r < len(s):
            if s[r] == s[r - 1] + 1:
                r = r + 1
                continue
            else:
                if len(s[l:r]) > longest:
                    longest = len(s[l:r])
                l = r
                r = l + 1

        if len(s[l:r]) > longest:
            longest = len(s[l:r])

        return longest