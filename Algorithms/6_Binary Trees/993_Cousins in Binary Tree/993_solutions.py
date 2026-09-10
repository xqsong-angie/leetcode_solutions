#20260720
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional
#https://algo.monster/liteproblems/993
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:#BFS
        """
        Determine if two nodes are cousins in a binary tree.
        Two nodes are cousins if they have the same depth but different parents.
      
        Args:
            root: Root node of the binary tree
            x: Value of the first node
            y: Value of the second node
          
        Returns:
            True if x and y are cousins, False otherwise
        """
        # Initialize queue for BFS with (node, parent) tuples
        queue = deque([(root, None)])
      
        # Track current depth level
        current_depth = 0
      
        # Variables to store parent and depth information for x and y
        parent_x = parent_y = None
        depth_x = depth_y = None
      
        # Perform level-order traversal (BFS)
        while queue:
            # Process all nodes at the current depth level
            level_size = len(queue)
          
            for _ in range(level_size):
                node, parent = queue.popleft()
              
                # Check if current node matches x or y(先找到x和y)
                if node.val == x:
                    parent_x = parent
                    depth_x = current_depth
                elif node.val == y:
                    parent_y = parent
                    depth_y = current_depth
              
                # Add children to queue for next level
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
          
            # Move to next depth level
            current_depth += 1
      
        # Cousins must have different parents but same depth
        return parent_x != parent_y and depth_x == depth_y
