def solution(lst):
    lst_copy=lst.deepcopy()
    for i in range(len(lst)):
        lst[i]=lst_copy.index(i)#🔥容易超时
    return lst
    
def solution(lst):
    n = len(lst)
    res = [0] * n
    
    # O(N) 一次遍历即可完成映射
    for i in range(n):
        res[lst[i]] = i
        
    return res
