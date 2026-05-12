# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTreePaths(self,cur: Optional[TreeNode],cur_path: List[str], sub_paths: List[str]) -> List[str]:
        if not cur:
            return []
        cur_path.append(str(cur.val))
        if not cur.left and not cur.right: #leaf 
            sub_paths.append("->".join(cur_path))
        else: #at least one
            self.findTreePaths(cur.left,cur_path.copy(),sub_paths)
            self.findTreePaths(cur.right,cur_path.copy(),sub_paths)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths=[]
        if not root:
            return all_paths
        else:
            cur_path=[]
            cur=root
            sub_paths=self.findTreePaths(cur,cur_path,all_paths)
            return all_paths