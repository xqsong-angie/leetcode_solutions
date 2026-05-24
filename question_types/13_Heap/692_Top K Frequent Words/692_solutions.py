from collections import Counter
import heapq
#https://www.geeksforgeeks.org/python/python-heapq-heappush-method/
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words) #{word:freq}
        
        heap = []
        res=[]
        for word, count in freq.items():
            heapq.heappush(heap, (-count, word)) #(priority, task),按priority排
        for _ in range(k): #python自动按字典序比较
            count,word=heapq.heappop(heap)
            res.append(word)

        return res