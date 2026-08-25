#20260823
from collections import Counter
import re
#错：
class Solution:
    def solution(self,members,messages):
        members_cnt=Counter(members)
        for m in messages:
            res1=re.search("^@[0-9]+ ",m)#🔥其实这道题可以完全不用正则，提及部分前后必须有空格，除非在开头或结尾。这意味着如果我们直接用 m.split() 把消息按空格切成单词列表，任何有效的 @mention 一定会独立成为一个单词！
            res2=re.search(" @[0-9]+$",m)
            res3=re.findall(" @[0-9]+ ",m)
            cur_set=set()
            if res1 or res2:#starts with or ends with
                if res1.group() not in cur_set:
                    members_cnt[res1.group()]+=1 #.group()只返回第一处
                    cur_set.add(res1.group())
                elif res2.group() not in cur_set:
                    members_cnt[res2.group()]+=1
                    cur_set.add(res2.group())
            elif res3:
                for r in res3:
                    if r not in cur_set:
                       members_cnt[r]+=1
                       cur_set.add(r)

        result=sorted(members_cnt.items(), key=lambda item: item[1])#🔥这里遇到tie的时候还需key字典序升序
        ans=[]
        for k,v in result.items():
            ans.append("["+k[1:]+"]=["+v+"]")
        return ans
    
#对：
class Solution:
    def solution(self, members: list[str], messages: list[str]) -> list[str]:
        mention_counts = {m: 0 for m in members}
        
        for m in messages:
            seen_in_msg = set()#🔥每个msg去重
            words = m.split()  # 按连续空格切分成单词列表
            
            for word in words:
                # 检查单词是不是以 @id 开头
                if word.startswith("@id"):
                    # 剥离前面的 @ 符号，再按逗号切分用户 ID 🔥处理多id的情况@id1,id123,id983
                    raw_ids = word[1:].split(",")
                    for user_id in raw_ids:
                        seen_in_msg.add(user_id)
                        
            # 统计当前消息里的有效成员
            for user_id in seen_in_msg:
                if user_id in mention_counts:
                    mention_counts[user_id] += 1
                    
        # 排序：次数降序 (-x[1])，ID 字典序升序 (x[0])
        sorted_members = sorted(mention_counts.items(), key=lambda x: (-x[1], x[0]))
        return [f"[{u}]=[{c}]" for u, c in sorted_members]