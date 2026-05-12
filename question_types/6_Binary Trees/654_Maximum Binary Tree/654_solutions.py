# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root=TreeNode()
        if not nums:
            return None
        else:
            root.val=max(nums)
            idx=nums.index(root.val)
            root.left=self.constructMaximumBinaryTree(nums[:idx])
            root.right=self.constructMaximumBinaryTree(nums[idx+1:])
            return root