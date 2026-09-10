from collections import defaultdict
class Solution:
    def solution(self,efficiency,ids,fire_resign_list):
        """
        efficiency:[1,2,3,4,5],
        ids:[1,2,1,1,2]
        fire_resign_list:[(3,2),(2,0)]
        """
        res=sum(efficiency)
        mymap=defaultdict(list)
        for i in range(len(ids)):
            mymap[ids[i]].append(efficiency[i])
            