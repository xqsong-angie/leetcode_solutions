#20260807
#https://algo.monster/liteproblems/1061 并查集
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Find the lexicographically smallest equivalent string using Union-Find.
      
        Given equivalence relationships between characters in s1 and s2,
        return the lexicographically smallest equivalent string for baseStr.
      
        Args:
            s1: First string defining equivalence relationships
            s2: Second string defining equivalence relationships (s1[i] ~ s2[i])
            baseStr: The base string to transform
          
        Returns:
            The lexicographically smallest equivalent string
        """
      
        def find(char_index: int) -> int:
            """
            Find the root parent of a character using path compression.
          
            Args:
                char_index: Index of the character (0-25 for 'a'-'z')
              
            Returns:
                The root parent index of the character
            """
            if parent[char_index] != char_index:
                # Path compression: directly connect to root
                parent[char_index] = find(parent[char_index])
            return parent[char_index]
      
        # Initialize parent array where each character is its own parent
        # Index 0 represents 'a', 1 represents 'b', etc.
        parent = list(range(26))#初始化每个字母自己是一个集合
      
        # Build equivalence relationships from s1 and s2
        for char1, char2 in zip(s1, s2):
            # Convert characters to indices (0-25)
            index1 = ord(char1) - ord('a')
            index2 = ord(char2) - ord('a')
          
            # Find root parents of both characters
            root1 = find(index1) #每个字母都化为根
            root2 = find(index2)
          
            # Union by rank: always attach larger root to smaller root
            # This ensures lexicographically smallest parent
            if root1 < root2:
                parent[root2] = root1 #根是最小的
            else:
                parent[root1] = root2
      
        # Transform baseStr to its lexicographically smallest equivalent
        result_chars = []
        for char in baseStr:
            # Find the root parent (smallest equivalent character)
            char_index = ord(char) - ord('a')
            smallest_index = find(char_index)
            # Convert back to character and add to result
            result_chars.append(chr(smallest_index + ord('a')))
      
        return ''.join(result_chars)
