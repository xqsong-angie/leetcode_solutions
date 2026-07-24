#20260720
#https://algo.monster/liteproblems/472
class Trie:
    """Trie (prefix tree) data structure for efficient string storage and retrieval."""
  
    def __init__(self):
        # Array to store 26 children nodes (one for each lowercase letter)
        self.children = [None] * 26
        # Flag to mark if current node represents end of a word
        self.is_end = False

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self
        for char in word:
            # Calculate index for the character (0-25)
            index = ord(char) - ord('a')
            # Create new node if path doesn't exist
            if node.children[index] is None:
                node.children[index] = Trie()
            # Move to the child node
            node = node.children[index]
        # Mark the last node as end of word
        node.is_end = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Find all concatenated words in a dictionary.
        A concatenated word is formed by combining two or more shorter words from the same dictionary.
        """
      
        def can_form_by_concatenation(word: str) -> bool:
            """
            Check if a word can be formed by concatenating other words in the trie.
            Uses DFS to try all possible splits of the word.
            """
            # Empty string means we successfully split the entire word
            if not word:
                return True
          
            node = trie
            # Try to match prefixes of the word
            for i, char in enumerate(word):
                index = ord(char) - ord('a')
                # If no matching path exists, word cannot be formed
                if node.children[index] is None:
                    return False
              
                node = node.children[index]
                # If we found a complete word, try to match the remaining part
                if node.is_end and can_form_by_concatenation(word[i + 1:]):#剩下的部分递归判断
                    return True
          
            return False

        # Initialize trie and result list
        trie = Trie()
        result = []
      
        # Sort words by length to ensure shorter words are added to trie first
        # This allows longer words to be formed from shorter ones
        words.sort(key=lambda word: len(word))#短单词不可能由长单词组成，提前返回
      
        for word in words:
            # Check if current word can be formed by concatenating existing words
            if can_form_by_concatenation(word):#说明当前trie里存在该长单词的各个部分，不需要再把该长单词放入trie
                result.append(word)
            else:
                # If not, add it to trie for future concatenations，但是当前这个单词就不能用来组成了,这个单词也不能被用作结果
                trie.insert(word)
      
        return result

#20260724 看了一遍