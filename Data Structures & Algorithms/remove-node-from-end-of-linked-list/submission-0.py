# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        for _ in range(n-1):
            stack.pop()
        
        rmv = stack.pop()

        dummy = ListNode()
        # Case where the remove is the first value of the linked list
        if not stack:
            return head.next

        prev = stack.pop()

        prev.next = rmv.next

        return head