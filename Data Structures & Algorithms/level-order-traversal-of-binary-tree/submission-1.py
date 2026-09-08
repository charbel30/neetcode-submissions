# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        array = []
       
        while queue:
            currarr = []
            for _ in range(len(queue)):
                Node = queue.popleft()
                currarr.append(Node.val)

                if Node.left:
                    queue.append(Node.left)
                if Node.right:
                    queue.append(Node.right)
            array.append(currarr)

        return array
