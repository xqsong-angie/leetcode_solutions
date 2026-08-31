#容易超时O（n^3)
class Solution:
    def solution(self,s):
        def isPalindrome(substring):
            i=0
            j=len(substring)-1
            while i<j:
                if substring[i]!=substring[j]:
                    return False
                else:
                    i+=1
                    j-=1
            return True
        
        res=0
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                substring=s[i:j+1]
                if isPalindrome(substring):
                    res+=1
        return res

#中心扩展法
class Solution:
    def solution(self, s: str) -> int:
        n = len(s)
        res = 0
        
        # 辅助函数：从 left 和 right 向两边扩展，并累加回文串数量
        def countPalindromes(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            # 1. 以 s[i] 为中心的奇数长度回文串
            res += countPalindromes(i, i)
            # 2. 以 s[i] 和 s[i+1] 之间的间隔为中心的偶数长度回文串
            res += countPalindromes(i, i + 1)
            
        return res