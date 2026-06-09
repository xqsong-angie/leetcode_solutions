# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self,left:Optional[TreeNode], right:Optional[TreeNode])->bool:
        if not left and right:
            return False
        elif left and not right:
            return False
        elif not left and not right:
            return True
        elif left.val !=right.val:
            return False
        else:#left.val==right.val
            return self.compare(left.left,right.right) and self.compare(left.right,right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left,root.right)

#20260608
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #https://algo.monster/liteproblems/101
        def is_mirror(left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
            """
            Helper function to check if two subtrees are mirror images of each other.
          
            Args:
                left_node: Root of the left subtree
                right_node: Root of the right subtree
              
            Returns:
                True if the subtrees are mirrors, False otherwise
            """
            # Both nodes are None - symmetric base case
            if left_node is None and right_node is None:
                return True
          
            # One node is None but not the other - not symmetric
            if left_node is None or right_node is None:
                return False
          
            # Values don't match - not symmetric
            if left_node.val != right_node.val:
                return False
          
            # Recursively check:
            # - left child of left_node with right child of right_node
            # - right child of left_node with left child of right_node
            return (is_mirror(left_node.left, right_node.right) and 
                    is_mirror(left_node.right, right_node.left))
      
        # An empty tree or single node is symmetric
        if root is None:
            return True
          
        # Check if left and right subtrees are mirrors of each other
        return is_mirror(root.left, root.right)