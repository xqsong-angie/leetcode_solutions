class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res=[]
        self.path=[]
        def isPalindrome(s,start,end)->bool:
            while start<end:
                if s[start]==s[end]:
                    start+=1
                    end-=1
                else:
                    return False
            return True

        def backtracking(s,pt)->None:
            if pt<len(s):
                for i in range(pt,len(s)):
                    if isPalindrome(s,pt,i):
                        self.path.append(s[pt:i+1])
                        backtracking(s,i+1)
                        self.path.pop()
            else:
                self.res.append(list(self.path))
        backtracking(s,0)
        return self.res