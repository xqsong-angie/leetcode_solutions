#20260620
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_splited=path.split("/")
        stack=[]
        n=len(path_splited)
        for i in range(n):
            if stack and path_splited[i]=="..":
                stack.pop()
            elif path_splited[i] and path_splited[i]!="." and path_splited[i]!="..":
                stack.append(path_splited[i])
        return "/"+"/".join(stack)