class LinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# Tip: self.tail is the current position of the Browser History
class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = LinkedList(homepage)
        self.tail = self.head

    def visit(self, url: str) -> None:
        new_node = LinkedList(url, next=None, prev=self.tail)
        
        # Update Tail Node
        self.tail.next = new_node
        self.tail = self.tail.next
        
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.tail.prev:
                self.tail = self.tail.prev
            else:
                return self.tail.val
        return self.tail.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.tail.next:
                self.tail = self.tail.next
            else:
                return self.tail.val
        return self.tail.val

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