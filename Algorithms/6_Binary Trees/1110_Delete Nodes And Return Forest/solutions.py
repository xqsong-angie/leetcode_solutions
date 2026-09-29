#20260929
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:#🔥TypeError: cannot use 'list' as a set element (unhashable type: 'list')
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        i=0
        if not root:
            return []
        elif not root.left and not root.right:
            if root.val==to_delete[i]:
                return []
            else:
                return [root]
        else:
            while i<len(to_delete):
                if root.val==to_delete[i]:#节点被删除时
                    to_delete.remove(to_delete[i])
                    left=self.delNodes(root.left,to_delete)#🔥当节点被删除时，它的左/右子节点应该成为新的树根（如果存在），需要加入答案列表中
                    right=self.delNodes(root.right,to_delete)
                    return [left]+[right]#🔥[left] + [right] 拼接出了嵌套列表
                    #🔥引申：如果使用[left,right]最后再flatten依然不行，因为无法区分“哪部分是子树根节点”，哪部分是“断开后产生的新树”
                else:#节点不被删除时
                    left=self.delNodes(root.left,to_delete)
                    right=self.delNodes(root.right,to_delete)
                    root.left=left
                    root.right=right
                    return [root]
                
#参考答案
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)  # 🔥转成 set，查找速度 O(1)，因为unique所以不需要每次删完去手动删除值
        res = []

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            # 1. 先递归处理左右子树（自底向上）
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            # 2. 判断当前节点是否需要删除
            if node.val in to_delete_set:
                # 如果当前节点要被删，它的左右子节点（如果还没被删）就会变成新的树根
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None  # 返回 None，让父节点指向 None（断开连接）
            
            return node  # 不需要删除，返回自身给父节点连接

        # 如果根节点没有被删除，根节点也是答案之一
        if dfs(root):
            res.append(root)
            
        return res
    
"""
你先看到 A 要被删，你把 A 删掉。

A 的下属有 B，因为 A 没了，按照规则 B 变成了“新树根”，你把 B 收集到了答案 res 中。

接着你往下走去处理 B，发现 B 也要被删！

你把 B 删掉了，把 B 的下属 C 收集到 res 中。

尴尬的事情发生了：你之前把 B 放进了 res，但现在 B 被删了，你还必须回头去 res 里面找到 B 并把它踢出去！这种“撤回”逻辑写起来会极其痛苦。
"""