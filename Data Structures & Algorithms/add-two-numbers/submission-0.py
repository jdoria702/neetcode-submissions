# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse both lists
        curr = l1
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head1 = prev
        
        curr = l2
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head2 = prev

        num1 = ""
        curr = head1
        while curr:
            num1 = num1 + str(curr.val)
            curr = curr.next
        
        num2 = ""
        curr = head2
        while curr:
            num2 = num2 + str(curr.val)
            curr = curr.next
        
        total = str(int(num1) + int(num2))
        dummy = ListNode()
        tail = dummy
        for c in total:
            tail.next = ListNode(int(c))
            tail = tail.next
    
        curr = dummy.next
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        ret_head = prev

        return ret_head
