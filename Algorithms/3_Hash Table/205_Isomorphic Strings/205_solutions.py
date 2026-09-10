#20260804
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map=defaultdict(str)
        t_map=defaultdict(str)
        for i in range(len(s)):
            if s[i] not in s_map and t[i] not in t_map or s[i] in s_map and s_map[s[i]]==t[i]:
                s_map[s[i]]=t[i]
                t_map[t[i]]=s[i]
            else:
                return False

        return True