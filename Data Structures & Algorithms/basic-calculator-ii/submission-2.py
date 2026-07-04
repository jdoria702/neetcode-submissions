class Solution:
    def calculate(self, s: str) -> int:
        s_clean = s.replace(" ", "")
        currNum = ""
        operation = "+"
        stack = []
        operations = ["+", "-", "*", "/"]
        for i, ch in enumerate(s_clean):
            if ch.isdigit():
                currNum = currNum + ch
            
            if ch in operations or i == len(s_clean) - 1:
                if operation == "+":
                    stack.append(int(currNum))
                    currNum = ""
                    operation = ch
                elif operation == "-":
                    stack.append(-1 * int(currNum))
                    currNum = ""
                    operation = ch
                elif operation == "*":
                    stack.append(stack.pop() * int(currNum))
                    currNum = ""
                    operation = ch
                else:
                    stack.append(math.trunc(stack.pop() / int(currNum)))
                    currNum = ""
                    operation = ch
        return sum(stack)
