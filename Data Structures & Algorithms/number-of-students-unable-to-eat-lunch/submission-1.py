class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Create a queue of students via Linked List for faster operations
    def initialize(self, students):
        for student in students:
            new_node = ListNode(student)

            # Create initial head and tails
            if self.head == None and self.tail == None:
                self.head = new_node
                self.tail = new_node
            # Update tail to point to new node and update tail position
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                
            # Update Length
            self.length += 1

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Convert from array to linked list
        self.initialize(students)
        unable_to_eat = 0

        # Do the queue
        while self.length > 0 and unable_to_eat < self.length:
            top_sandwich = sandwiches[0]

            # Check if last student at queue likes the sandwich
            if self.head.val == top_sandwich:
                # remove student & sandwich
                if self.length > 1:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    self.head = None
                    self.tail = None
            
                sandwiches.pop(0)
                self.length -= 1
                unable_to_eat = 0
            
            # Student queues back
            else:
                # Edge case: only one student left
                if self.length > 1:
                    first = self.head
                    self.head = self.head.next
                    self.head.prev = None

                    self.tail.next = first
                    first.prev = self.tail
                    first.next = None
                    self.tail = first

                unable_to_eat += 1

        # Number of Students Left
        return self.length

    def debug(self):
        current = self.head
        while current:
            value = current.val
            print(current.val, current.prev, current.next)
            current = current.next


