#20260705
#错（超时） O（n^2)：
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited=set()
        n=len(strs)
        res=[]
        for i in range(n):
            if strs[i] not in visited:
                str_cnt=Counter(strs[i])
                path=[strs[i]]
                visited.add(strs[i])
                for j in range(i+1,n):
                    if Counter(strs[j])==str_cnt:
                        path.append(strs[j])
                        visited.add(strs[j])
                res.append(list(path))
        return res
#对O（NK)K是列表里最长字符串的长度：
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            # 创建一个长度为 26 的列表，记录每个字母的出现次数
            count = [0] * 26
            for char in s:
                # ord() 提取字符的 ASCII 码，减去 'a' 的 ASCII 码即可映射到 0-25
                count[ord(char) - ord('a')] += 1
            
            # 将列表转换为元组作为字典的键 (元组是不可变的，可以被 hash)
            anagrams[tuple(count)].append(s)
            
        return list(anagrams.values())