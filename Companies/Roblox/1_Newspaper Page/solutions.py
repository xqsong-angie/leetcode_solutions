#20260822
#错：🙂
class Solution:
    def newspaperPage(paragraphs, aligns, width):
        res=[]
        for i in range(paragraphs): # each paras 🔥list要用len()做range
            count=0 #current num of chars
            string=""
            path=[]
            for j in range(paragraphs[i]): # each words
                if count+len(paragraphs[i][j])<=width:#🔥要加空格的长度
                    count+=len(paragraphs[i][j])#🔥要加空格的长度
                    path.append(paragraphs[i][j]) #🔥如果path到最后了也没满，需要单独把这一行加进去
                else:
                    if aligns[i]=="LEFT":#🔥左右逻辑反了
                        string="*"+" "*(width-count)+" ".join(path)+"*"
                    else:
                        string="*"+" ".join(path)+" "*(width-count)+"*"
                        count=0#new line 🔥path也要归零，string也要归零，而且这个操作要写在当前else外面，否则aligns[i]=="LEFT"没有重置
                    res.append(string)
                    
        return ["*"*(width+2)]+res+["*"*(width+2)]


#对：
class Solution:
    def newspaperPage(self, paragraphs, aligns, width):
        res=[]
        for i in range(len(paragraphs)): # each paras
            count=0 #current num of chars
            string=""
            path=[]
            for j in range(len(paragraphs[i])): # each words
                needed_space = len(paragraphs[i][j]) if count == 0 else len(paragraphs[i][j]) + 1 #🔥动态判断所需长度

                if count+needed_space<=width:
                    count+=needed_space
                    path.append(paragraphs[i][j]) 
                else:
                    if aligns[i]=="LEFT":
                        string="*"+" ".join(path)+" "*(width-count)+"*"
                    else:
                        string="*"+" "*(width-count)+" ".join(path)+"*"
                    res.append(string)
                    count=len(paragraphs[i][j])#new count
                    path=[paragraphs[i][j]] #new path
                    string=paragraphs[i][j] #new line

            if path:
                if aligns[i]=="LEFT":
                    string="*"+" ".join(path)+" "*(width-count)+"*"
                else:
                    string="*"+" "*(width-count)+" ".join(path)+"*"
                res.append(string)
                
                    
        return ["*"*(width+2)]+res+["*"*(width+2)]			
					