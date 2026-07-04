class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(substr: str):
            l = 0
            r = len(substr) - 1
            while l < r:
                if substr[l] != substr[r]:
                    return False
                l = l + 1
                r = r - 1
            return True
        
        l = 0   
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if isPalindrome(s[l:r]):
                    return True
                elif isPalindrome(s[l+1:r+1]):
                    return True
                else:
                    return False
            l = l + 1
            r = r - 1
        return True