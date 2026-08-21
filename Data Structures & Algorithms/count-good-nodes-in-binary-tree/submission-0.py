# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def isGood(root, max_val):
            if root == None:
                return 0


            count = 0

            if root.val >= max_val:
                count = 1

            max_val = max(root.val, max_val)

            count += isGood(root.left, max_val)

            count += isGood(root.right, max_val)


            return count


        return isGood(root, root.val)

        