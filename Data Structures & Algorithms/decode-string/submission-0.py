class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = ""
        
        for ch in s:
            if ch.isdigit():
                num = num + ch
            if ch.isalpha():
                cur = cur + ch
            if ch == "[":
                stack.append((cur, int(num)))
                cur = ""
                num = ""
            if ch == "]":
                popped = stack.pop()
                cur = popped[0] + (cur * popped[1])
            
        return cur