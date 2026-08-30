class LinkNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyStack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        new_node = LinkNode(x)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self) -> int:
        result = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            previous_node = self.tail.prev
            previous_node.next = None
            self.tail = previous_node

        return result.val

    def top(self) -> int:
        if self.head:
            return self.tail.val
        

    def empty(self) -> bool:
        if self.head == None and self.tail == None:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()