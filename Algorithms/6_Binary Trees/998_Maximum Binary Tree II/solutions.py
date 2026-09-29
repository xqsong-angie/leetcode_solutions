#20260928
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode | None, val: int) -> TreeNode | None:
        b=root
        def helper(root,val):#🔥Suppose b is a copy of a with the value val appended to it
            if root.val<val:#🔥val插入数组的末尾，所以一定在右子树，题目理解错，新值不能出现在左子树
                new_root=TreeNode(val=val)
                new_root.left=root
                return new_root
            else:
                if root.left and root.right:
                    left=helper(root.left,val)
                    right=helper(root.right,val)
                    if left.val==val:
                        root.left=left
                        return root
                    elif right.val==val:
                        root.right=right
                        return root

                elif not root.left or not root.right:
                    new_node=TreeNode(val=val)#🔥这里同样问题，不可以挂在左子树上
                    if not root.right:
                        root.right=new_node
                    if not root.left:
                        root.left=new_node
                    return root

        return helper(b,val) 
    

#参考答案
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # 基准情况：如果走到空位置，或者新值大于当前节点的值
        if not root or val > root.val:
            node = TreeNode(val)
            node.left = root  # 🔥旧子树成为新节点的左子树（因为新节点在原数组右侧），注意数组特性
            return node
        
        # 如果 val < root.val，新节点必定在右子树中，向右递归
        root.right = self.insertIntoMaxTree(root.right, val)
        return root