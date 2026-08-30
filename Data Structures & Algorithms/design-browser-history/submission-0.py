class LinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = LinkedList(homepage)
        self.head = self.current
        self.tail = self.current

    def visit(self, url: str) -> None:
        new_node = LinkedList(url, next=None, prev=self.current)
        
        # Update Current Node
        self.current.next = new_node
        self.current = self.current.next

        # Sync Tail Node to current Node
        self.tail = new_node
        
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev:
                self.current = self.current.prev
            else:
                return self.current.val
        print(self.current.val)
        return self.current.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next:
                self.current = self.current.next
            else:
                return self.current.val
        print(self.current.val)
        return self.current.val

    def debug(self):
        iterator = self.head
        while iterator:
            print(iterator.val)
            iterator = iterator.next
        print("#########\n")

    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)