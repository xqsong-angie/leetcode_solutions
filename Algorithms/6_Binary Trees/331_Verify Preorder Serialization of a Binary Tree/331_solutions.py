#20260928
class Solution:
    def helper(self,preorder_split,pt):
        if len(preorder_split[pt:]==1):
            if preorder_split[pt].isdigit():
                return False
            else:
                return True
        #🔥到这里的时候发现确定不了遍历顺序
        else:   
            if self.helper(preorder_split[pt+1:]):
                return True
            else:
                return False

    def isValidSerialization(self, preorder: str) -> bool:
        if len(preorder)==1:#no root
            if preorder.isdigit():
                return False
            else:
                return True
        else:#root
            preorder_split=preorder.split(",")
            if "#" not in preorder_split:
                return False
            return self.helper(preorder_split,0)

#参考答案
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1  # 初始槽位（根节点位置）
        
        for node in preorder.split(','):
            # 每遇到一个节点，先消耗 1 个槽位
            slots -= 1
            
            # 槽位不够了，说明序列提前中断或格式非法
            if slots < 0:
                return False
            
            # 如果是非空节点，会提供 2 个新的槽位，这两个槽位可以是#也可以是数字
            if node != '#':#🔥不需要.isdigit()
                slots += 2
                
        # 遍历完成后，槽位必须恰好被填满
        return slots == 0