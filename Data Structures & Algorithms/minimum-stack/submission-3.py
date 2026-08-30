class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        # Append Number to stack
        self.stack.append(val)

        # Add to minstack without comparison if empty
        if len(self.minstack) == 0 or self.minstack[len(self.minstack) - 1] >= val:
            self.minstack.append(val) 
    
    def pop(self) -> None:
        # pop from stack
        num = self.stack.pop()

        # pop from minstack
        last_idx = len(self.minstack) - 1
        if self.minstack[last_idx] == num:
            self.minstack.pop()


    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minstack[len(self.minstack) - 1]