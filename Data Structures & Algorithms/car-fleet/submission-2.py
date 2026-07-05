class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Monotonically increasing stack
        Each entry in the stack represents a fleet

        Algorithm:
            1. Group position and speed and sort by position
            2. Calculate time to finish (TTF) by dividing target - position / speed (ceiling)
            3. Iterate backwards and create monotonically increasing stack
                a. if TTF is less than top of stack: do not add. It becomes part of fleet
                b. if TTF is greater: add to stack. It is its own fleet
            4. Return length of stack
        """

        # (position, TTF)
        sorted_cars = []
        for i in range(len(position)):
            TTF = (target - position[i]) / speed[i]
            sorted_cars.append((position[i], TTF))

        sorted_cars.sort()
        
        stack = []
        for i in range(len(sorted_cars) - 1, -1, -1):
            if not stack:
                stack.append(sorted_cars[i][1])
                continue
            
            if sorted_cars[i][1] > stack[-1]:
                stack.append(sorted_cars[i][1])

        return len(stack)