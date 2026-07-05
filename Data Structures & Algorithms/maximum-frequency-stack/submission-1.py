class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.count = {}
        self.stacks = {}
        

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1

        self.stacks[self.count[val]] = self.stacks.get(self.count[val], []) + [val]

        if self.count[val] > self.max_freq:
            self.max_freq = self.count[val]
        
        return
        
        

    def pop(self) -> int:
        max_freq_list = self.stacks.get(self.max_freq)
        ret = max_freq_list.pop()

        self.count[ret] = self.count[ret] - 1

        if not max_freq_list:
            self.max_freq = self.max_freq - 1
        
        return ret
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()