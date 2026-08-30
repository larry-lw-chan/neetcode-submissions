# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Tail is the head of the reverse list
        tail = None

        # Edge Case Handling
        if not hasattr(head, "next"): return tail
        
        while True:
            lastNode = head
            secondLastNode = None

            # Iterate to find last node
            while lastNode.next != None:
                secondLastNode = lastNode
                lastNode = lastNode.next

            # Create reverseHead if None
            if tail == None:
                tail = lastNode
            else:
                # Iterate to find last reverse node
                reverseNode = tail
                while reverseNode.next != None:
                    reverseNode = reverseNode.next
                # Assign reverseNode
                reverseNode.next = lastNode

            # Check for condition and break
            if head.next == None: 
                break
            else:
                secondLastNode.next = None

        return tail