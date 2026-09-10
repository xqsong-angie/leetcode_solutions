# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self,cur: Optional[TreeNode])->int:
        if not cur:#子树没有根节点
            return 0
        elif not cur.left and not cur.right:##子树只有根节点
            return 1
        else:
            return 1+max(self.getHeight(cur.left),self.getHeight(cur.right))#子树有left or right,取两者更大值

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:#空树肯定平衡
            return True
        else:
            cur=root
            if abs(self.getHeight(cur.left)-self.getHeight(cur.right))<=1:#平衡定义：左右子树高度相差绝对值不超过1
                return self.isBalanced(cur.left) and self.isBalanced(cur.right)#🔥母树平衡，子树不平衡[1,2,3,4,null,null,5,6,null,null,7]
            else:#子树平衡，母树不平衡，提前剪枝[1, 2, 3, 4, null, null, null, 5]
                return False
            
#20260709 看了一遍
#自底向上遍历，更好
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:#树上的任意一个节点，其左右子树的高度差都不能超过 1
        # 如果最终返回的不是 -1，说明整棵树是平衡的
        return self.checkHeight(root) != -1

    def checkHeight(self, cur: Optional[TreeNode]) -> int:
        if not cur:
            return 0  # 空节点高度为 0，自然也是平衡的
        
        # 1. 先去左边看（一路到底）
        left_height = self.checkHeight(cur.left)
        if left_height == -1: 
            return -1  # 左子树不平衡，提前熔断，直接返回 -1
            
        # 2. 再去右边看
        right_height = self.checkHeight(cur.right)
        if right_height == -1: 
            return -1  # 右子树不平衡，提前熔断，直接返回 -1
        
        # 3. 左右都看完了，回到当前节点自己（后序：左右根）
        if abs(left_height - right_height) > 1:
            return -1  # 当前节点这一级不平衡了，返回 -1
        else:
            # 没问题，返回当前节点作为母树时的真实高度
            return max(left_height, right_height) + 1