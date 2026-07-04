class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = []

        # calculate time needed to reach destination for each car
        for i in range(len(position)):
            time_needed = (target - position[i]) / speed[i]
            time.append((time_needed, position[i]))
        
        
        time_sorted = sorted(time, reverse=True, key=lambda x: x[1])
        
        for time, _ in time_sorted:
            if not stack:
                stack.append(time)
            
            # Case: car behind is faster --> ignore car
            if time <= stack[-1]:
                continue
            # Case: car behind is slower --> create new fleet
            else:
                stack.append(time)
            
        return len(stack)


