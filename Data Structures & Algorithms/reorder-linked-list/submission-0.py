# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # TC: O(n)
        # SC: O(1)
        # Find middle of the linked list
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # TC: O(n)
        # SC: O(1)
        # Split the list in two
        #   - Slow will point at None
        #   - Reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head2 = prev

        # TC: O(n)
        # SC: O(1)
        # Merge
        curr1 = head
        curr2 = head2
        dummy = ListNode()
        tail = dummy
        while curr1 and curr2:
            tail.next = curr1
            tmp1 = curr1.next
            tail = tail.next

            tail.next = curr2
            tmp2 = curr2.next
            tail = tail.next

            curr1 = tmp1
            curr2 = tmp2

        # TC: O(1)
        # SC: O(1)
        # Append the remaining longer list to the tail
        if curr1:
            tail.next = curr1
        elif curr2:
            tail.next = curr2

        return

            