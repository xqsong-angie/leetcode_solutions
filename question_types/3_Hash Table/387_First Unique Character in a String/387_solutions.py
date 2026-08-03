#20260803
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        hash_map={}
        for i in range(n):
            if s[i] in hash_map:
                hash_map[s[i]]=n
            else:
                hash_map[s[i]]=i
        res=hash_map[min(hash_map,key=hash_map.get)]
        return res if res<n else -1