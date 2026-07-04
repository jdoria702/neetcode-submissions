# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # LCA is the moment p and q end up in different subtrees

        # LCA is also the moment p.val or q.val equals the curr.val

        # Keep searching if p.val and q.val are in the same next subtree

        curr = root
        while curr:
            if (p.val < curr.val and q.val > curr.val) or (p.val > curr.val and q.val < curr.val):
                return curr
        
            if p.val == curr.val or q.val == curr.val:
                return curr
            
            if p.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None