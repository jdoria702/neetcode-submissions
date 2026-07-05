class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = ""
        
        for ch in s:
            if ch.isdigit():
                num = num + ch
            elif ch.isalpha():
                cur = cur + ch
            elif ch == "[":
                stack.append((cur, int(num)))
                cur = ""
                num = ""
            elif ch == "]":
                popped = stack.pop()
                cur = popped[0] + (cur * popped[1])
            
        return cur