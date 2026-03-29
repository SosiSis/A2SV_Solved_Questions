# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
   
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
      
        stack = []
        for value in values:

            while stack and stack[-1] < value:
                stack.pop()
            stack.append(value)
      
        dummy_head = ListNode()
        current = dummy_head
        for value in stack:
            current.next = ListNode(value)
            current = current.next
          
        return dummy_head.next