class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res=[]
        self.path=[]
        def isValidInt(seg):
            if not seg:
                return False
            elif len(seg)>3:
                return False
            elif (seg.startswith("0") and len(seg)>1) or int(seg)>255:
                return False
            else:
                return True
        
        def backtracking(s,pt,count):
            if pt<len(s) and count<3:
                for i in range(pt,len(s)):
                    if isValidInt(s[pt:i+1]):
                        self.path.append(s[pt:i+1])
                        backtracking(s,i+1,count+1)
                        self.path.pop()
            elif count==3:
                if isValidInt(s[pt:]):
                    self.path.append(s[pt:])
                    self.res.append(".".join(self.path))
                    self.path.pop()
                else:
                    return
                
        backtracking(s,0,0)
        return self.res

