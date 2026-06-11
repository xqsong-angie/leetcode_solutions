class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        str_shuffled=[""]*n
        for i in range(n):
            str_shuffled[indices[i]]=s[i]
        return "".join(str_shuffled)