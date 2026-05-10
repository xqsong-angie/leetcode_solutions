class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        for i in range(len(s_list)):
            s_list[i] = s_list[i].strip()
        left=0
        n=len(s_list)
        right=n-1
        while left<right:
            temp=s_list[left]
            s_list[left]=s_list[right]
            s_list[right]=temp
            left+=1
            right-=1
        

        return " ".join(s_list)
