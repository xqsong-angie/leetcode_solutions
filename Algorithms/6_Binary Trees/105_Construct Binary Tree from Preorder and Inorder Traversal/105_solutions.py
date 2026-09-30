#20260930
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#我是想通过前序构建树，然后用中序判断具体衔接位置🔥这个思路是没问题的，实现方式太复杂了
class Solution:
    def helper(self,val):
        root=TreeNode(val)
        root.left=self.helper()#这里我想换一个val,但是不知道怎么写，之前只写过前序遍历，没写过前序构建
        root.right=self.helper()
        return root
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        n=len(preorder)
        if n==1:
            return TreeNode(val=preorder[0])
        else:
            root=TreeNode(val=preorder[0])#https://www.geeksforgeeks.org/python/python-list-index/
            prev=inorder.index(preorder[0])
            cur=root
            for i in range(1,n):
                if inorder.index(preorder[i])<inorder.index(prev): #left subtree
                    new_node=TreeNode(preorder[i])

#答案
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # 递归终止条件：列表为空说明已经没有节点了，返回 None
        if not preorder or not inorder:
            return None
        
        # 1. 前序遍历的第一个节点即为根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. 在中序遍历中找到根节点的索引，🔥划分左右子树
        mid = inorder.index(root_val)#🔥根的index左边的所有元素是左子树，右边所有元素是右子树
        
        # 3. 递归构建左子树和右子树
        # mid 表示左子树的节点数量
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root