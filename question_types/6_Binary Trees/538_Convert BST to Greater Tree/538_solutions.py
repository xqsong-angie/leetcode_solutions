# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.prev=0#得保存前一个，其实就是当前节点加上上一个大结果
        def traversal(root):
            if not root:
                return 
            else:#中序遍历改为右左中即可
                traversal(root.right)#一直把指针挪到最右侧
                root.val+=self.prev#累加
                self.prev=root.val#更新
                traversal(root.left)#
        traversal(root)
        return root

#20260711 看了一遍