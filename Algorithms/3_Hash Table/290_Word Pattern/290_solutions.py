#20260705
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list=s.split(" ")
        key_map=defaultdict(str)
        value_map=defaultdict(str)
        if len(pattern)!=len(s_list):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in key_map.keys() and s_list[i] not in value_map.keys():
                    key_map[pattern[i]]=s_list[i]
                    value_map[s_list[i]]=pattern[i]
                else:
                    if key_map[pattern[i]]!=s_list[i] or value_map[s_list[i]]!=pattern[i]:
                        return False
            return True