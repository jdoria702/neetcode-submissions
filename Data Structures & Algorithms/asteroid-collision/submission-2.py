class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        stack.append(asteroids[0])

        for i in range(1, len(asteroids)):
            # Non colliding asteroid
            if not stack or stack[-1] < 0 or (stack[-1] > 0 and asteroids[i] > 0):
                stack.append(asteroids[i])
                continue
            
            # Oncoming asteroid
            while stack[-1] > 0 and abs(stack[-1]) < abs(asteroids[i]):
                stack.pop()
                # Oncoming beat all right-going asteroids
                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
                    continue
            
            # Incoming and outcoming asteroid both exploded
            if stack[-1] > 0 and abs(stack[-1]) == abs(asteroids[i]):
                stack.pop()
                continue
            
        return stack