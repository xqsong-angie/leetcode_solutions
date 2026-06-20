#20260619
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #https://www.geeksforgeeks.org/python/python-sort-values-first-list-using-second-list/
        #https://www.reddit.com/r/PythonLearning/comments/1l3vy2r/how_to_use_sorted_function_with_reversetrue/
        x = [val for _, val in sorted(zip(heights, names),reverse=True)] #列表推导式掌握不熟
        return x
