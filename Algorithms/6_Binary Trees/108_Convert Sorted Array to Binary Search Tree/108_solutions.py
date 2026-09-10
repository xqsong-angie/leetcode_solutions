# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        else:
            length=len(nums)//2
            root=TreeNode(val=nums[length])
            root.left=self.sortedArrayToBST(nums[:length])
            root.right=self.sortedArrayToBST(nums[length+1:])
            return root