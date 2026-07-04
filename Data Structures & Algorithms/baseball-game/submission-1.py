class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * int(stack[-1]))
            else:
                stack.append(int(op))
        return sum(stack)