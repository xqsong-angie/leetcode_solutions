from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
    
        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, length = queue.popleft()#上一个词，length是path length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]#每一个word的每一个位置都试图替换一个字母
                    if new_word in wordSet and new_word not in visited:#没有的话就可以添加到path中
                        if new_word == endWord:
                            return length + 1#Path结束
                        visited.add(new_word)
                        queue.append((new_word, length + 1))#在无权图（每一步的代价都是 1）中，BFS 第一次找到 endWord 时，所经过的路径就一定是绝对最短的！
        
        return 0
    
#20260723 看了一遍