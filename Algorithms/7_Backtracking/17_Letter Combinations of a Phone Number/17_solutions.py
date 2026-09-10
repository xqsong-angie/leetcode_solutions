class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res=[]
        self.path=""
        map={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def backtracking(digits,start_dgt):
            if start_dgt<len(digits):
                letters=map[digits[start_dgt]]
                for l in letters:
                    self.path+=l
                    backtracking(digits,start_dgt+1)
                    self.path=self.path[:-1]
            else:
                self.res.append(self.path)
        backtracking(digits,0)
        return self.res