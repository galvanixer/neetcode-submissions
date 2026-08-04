class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.min = float('inf')


    def push(self, val:int) -> None:
        self.stack.append(val)
        self.minstack.append(min(val, self.minstack[-1])if self.minstack else val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
    
    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minstack[-1]


        
    # def __init__(self):
    #     self.stack = []
    #     self.min_stack = []
    #     self.min = float('inf')
        

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     val = min(val, self.min_stack[-1] if self.min_stack else val)
    #     self.min_stack.append(val)
        

    # def pop(self) -> None:
    #     self.min_stack.pop()
    #     return self.stack.pop()
        

    # def top(self) -> int:
    #     return self.stack[-1]
        
    # def getMin(self) -> int:
    #     return self.min_stack[-1]
        
