class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            print(f'i: {i}')
            print(f'stack: {stack}')
            print(f'result: {result}')
            if not stack:
                stack.append((temperatures[i], i))
                continue

            if temperatures[i] >= stack[-1][0]:
                while stack and temperatures[i] >= stack[-1][0]:
                    stack.pop()
                if len(stack) == 0:
                    stack.append((temperatures[i], i))
                    continue
                else:
                    result[i] = stack[-1][1] - i
                    stack.append((temperatures[i], i))
            else:
                result[i] = stack[-1][1] - i
                stack.append((temperatures[i], i))
        return result
    
