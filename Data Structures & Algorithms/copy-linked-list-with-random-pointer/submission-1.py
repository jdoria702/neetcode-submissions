"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a new node for each node in the original linked list
        # Use a hashmap to store the deep copy
        # Key: Original Node
        # Value: Deep Copy Node

        # First pass create a deep copy of each node
        hmap = {}
        curr = head
        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass assign next and random to each deep copy
        # Access next and random from the original
        curr = head
        while curr:
            copyNode = hmap[curr]
            copyNode.next = hmap.get(curr.next)
            copyNode.random = hmap.get(curr.random)
            curr = curr.next
        
        return hmap.get(head)