# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        array = []
        array.append(root.val)
        while queue:
            for _ in range(len(queue)):
                Node = queue.popleft()
                if Node.left:
                    queue.append(Node.left)
                if Node.right:
                    queue.append(Node.right)
            if queue:
                array.append(queue[-1].val)
        
                
        
        return array



