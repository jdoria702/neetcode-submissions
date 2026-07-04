class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(eval(f"{str(operand1)} {token} {str(operand2)}")))
            else:
                stack.append(token)
        return int(stack[-1])