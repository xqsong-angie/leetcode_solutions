# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:#分两步，先搜再删，如果搜不到就不删了
        if not root:
            return root
        elif key==root.val:#搜到了
            if not root.left and not root.right:
                return None#左右都没有，直接把整个子树都端了
            elif not root.left: #and root.right 没左有右，就用右子树填补空位
                return root.right
            elif not root.right: #and root.left 没右有左，就用左子树填补空位
                return root.left
            else: #root.left and root.right 两个都有，任选一个填补空位，另一个直接接上
                cur=root.left #这里我们以用左子树补位为例
                while cur.right:#左子树的右子树
                    cur=cur.right
                cur.right=root.right#把根节点右子树插到左子树最右侧
                return root.left#用左子树补根节点的位置
        elif key<root.val:#暂时没搜到，小了，说明可能在根节点左子树里面
            if not root.left:#如果根节点就没有左子树，那确实找不到
                return root
            else:#还有希望，接着把左子树当根搜
                root.left=self.deleteNode(root.left,key)
        elif key>root.val:#暂时没搜到，大了，说明可能在根节点右子树里面
            if not root.right:#如果根节点就没有右子树，那确实找不到
                return root
            else:#还有希望，接着把右子树当根搜
                root.right=self.deleteNode(root.right,key)
        return root#返回最后删好的新树
            
#20260710 看了一遍


