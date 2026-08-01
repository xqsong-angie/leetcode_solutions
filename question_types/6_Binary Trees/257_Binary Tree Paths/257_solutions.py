# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTreePaths(self,cur: Optional[TreeNode],cur_path: List[str], sub_paths: List[str]) -> List[str]:
        if not cur:
            return
        cur_path.append(str(cur.val))
        if not cur.left and not cur.right: #leaf 
            sub_paths.append("->".join(cur_path))
        else: #at least one
            self.findTreePaths(cur.left,cur_path.copy(),sub_paths)
            self.findTreePaths(cur.right,cur_path.copy(),sub_paths)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths=[]
        if not root:#空树
            return all_paths
        else:
            cur_path=[]
            cur=root
            self.findTreePaths(cur,cur_path,all_paths)
            return all_paths
        
#20260709 看了一遍

#20260728
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPaths(self, root,path,res):
        if not root.left and not root.right:
            path+=(str(root.val))
            res.append(path)
        else:
            if root.left:
                path+=(str(root.val)+"->")
                temp=len((str(root.val)+"->"))
                self.findPaths(root.left,path,res)
                path=path[:-temp]
            if root.right:
                path+=(str(root.val)+"->")
                temp=len((str(root.val)+"->"))
                self.findPaths(root.right,path,res)
                path=path[:-temp]

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        else:
            res=[]
            self.findPaths(root,"",res)
            return res