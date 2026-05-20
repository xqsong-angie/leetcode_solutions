from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def countDiff(w1, w2):
            return sum(c1 != c2 for c1, c2 in zip(w1, w2))
        
        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet and new_word not in visited:
                        if new_word == endWord:
                            return length + 1
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
        
        return 0