"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]
"""

# Recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            results.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return results

  """
  Results

  Runtime: Beats 100%
  Memory Beats 50%
  """

# Iterative Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       res = []
       stack = []
       cur = root

       while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
       return res

"""
Results

Runtime: beats 100%
Memory: Beats 7%
"""
