class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num_string = "".join(char.lower() for char in s if char.isalnum())
        
        l = 0
        r = len(alpha_num_string) - 1
        while l < r:
            if alpha_num_string[l] != alpha_num_string[r]:
                return False
            else:
                l = l + 1
                r = r - 1
                continue
        return True