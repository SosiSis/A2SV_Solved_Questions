# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=0
        my_list=[]
        current=head
        while current:

            my_list.append(current.val)
            current=current.next
        n=len(my_list)
        for i in range(n//2):
            twin= n-1-i
            sum=my_list[i] + my_list[twin]
            res=max(sum,res)   
        return res     
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna