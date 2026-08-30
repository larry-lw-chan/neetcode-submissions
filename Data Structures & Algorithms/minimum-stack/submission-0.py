class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # Only push int, else ignore invalid datatype
        if (type(val) is int):
            self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        min_num = self.stack[0]
        for num in self.stack:
            if num < min_num:
                min_num = num

        return min_num
        
