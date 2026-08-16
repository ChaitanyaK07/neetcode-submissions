from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        if root is None:
            return res

        queue = deque([root])

        while queue:

            n = len(queue)

            for i in range(n):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                if i == n - 1:
                    res.append(node.val)

        return res