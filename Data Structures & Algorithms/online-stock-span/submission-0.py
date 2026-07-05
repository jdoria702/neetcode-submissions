class StockSpanner:

    def __init__(self):
        # Monotonically decreasing stack
        self.stack = []
        

    def next(self, price: int) -> int:
        curr = [price, 1]
        if not self.stack:
            self.stack.append(curr)
            return curr[1]
        
        # Case 1: The price is smaller than the top of stack
        if curr[0] < self.stack[-1][0]:
            self.stack.append(curr)
            return curr[1]
        
        # Case 2: The price is larger than the top of stack
        #   - Keep accumulating the next values associated with the stack's top
        #   - Stop when the top of stack has a larger value or when stack is empty
        while self.stack and curr[0] >= self.stack[-1][0]:
            popped = self.stack.pop()
            curr[1] = curr[1] + popped[1]
        
        self.stack.append(curr)
        return curr[1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)