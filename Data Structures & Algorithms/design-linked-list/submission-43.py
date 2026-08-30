class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        # Return -1 for edge cases
        if index < 0 or index >= self.length:
            return -1     

        # Calculate current
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val
        
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, next=self.head, prev=None)

        if self.head:
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val, next=None, prev=self.tail)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node
        self.length += 1
        self.debug()

    def addAtIndex(self, index: int, val: int) -> None:
        # Don't insert if index greater than the length
        if index < 0 or index > self.length: 
            return

        # Perform add at head
        if index == 0:
            self.addAtHead(val)
            return

        # Perform add at tail on end of index
        if index == self.length:
            self.addAtTail(val)
            return

        # Deal with the middle
        current = self.head
        for _ in range(index):
            current = current.next

        # If index is equal to the length, then insert node 
        prev_node = current.prev
        new_node = ListNode(val, next=current, prev=prev_node)

        # Update
        prev_node.next = new_node
        current.prev = new_node
        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        # Handle edge case
        if index < 0 or index >= self.length: 
            return
        
        # If there's only one node
        if self.length == 1 and index == 0:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        # Do Algo
        current = self.head
        for _ in range(index):
            current = current.next

        # If last node is selected
        if index == self.length - 1:
            prev_node = current.prev
            prev_node.next = None
            self.tail = prev_node

        # If middle node is selected
        else:
            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next_node.prev = prev_node

        # Update length
        self.length -= 1

    def debug(self):
        current = self.head
        while current:
            print(f"{current.val}")
            current = current.next
        print("##########\n")


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(1)
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# obj.deleteAtIndex(index)