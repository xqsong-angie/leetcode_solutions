#错：
class Solution:
    def breakPalindrome(self,palindromeStr):
        res=""
        flag=False
        for i in range(len(palindromeStr)//2):#🔥没有考虑长度为1的情况
            if palindromeStr[i]=='a':
                res+=palindromeStr[i]
            else:
                res+="a"
                flag=True
                break#🔥原字符串剩余的所有字符都被遗漏了
        return res if flag==True else "IMPOSSIBLE"
            
#对：
class Solution:
    def breakPalindrome(self,palindromeStr):
        res=""
        flag=False
        n=len(palindromeStr)
        if n <= 1:
            return "IMPOSSIBLE"
        
        for i in range(n//2):
            if palindromeStr[i]=='a':
                res+=palindromeStr[i]
            else:
                res+="a"
                res += palindromeStr[i + 1:]#🔥拼接被替换位置后面的所有剩余字符
                flag=True
                break

        return res if flag==True else "IMPOSSIBLE"
