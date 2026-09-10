#20260807
#https://algo.monster/liteproblems/1163
class Solution:
    def lastSubstring(self, s: str) -> str:
        """
        Find the lexicographically largest substring of the given string.
        The largest substring will always be a suffix of the original string.
      
        Uses a two-pointer approach with comparison offset to efficiently find
        the starting position of the lexicographically largest suffix.
      
        Args:
            s: Input string
          
        Returns:
            The lexicographically largest substring (suffix)
        """
        # Initialize two pointers for comparing potential starting positions
        left_start = 0   # First candidate starting position
        right_start = 1  # Second candidate starting position
        offset = 0       # Current comparison offset from both starting positions
      
        # Continue until we've examined all necessary characters
        while right_start + offset < len(s):
            # Case 1: Characters at current offset are equal
            if s[left_start + offset] == s[right_start + offset]:
                # Move to next character for comparison
                offset += 1
              
            # Case 2: Left substring is smaller at current offset
            elif s[left_start + offset] < s[right_start + offset]:
                # Skip the entire left substring and its compared portion
                # The new left_start jumps past all compared characters
                left_start = left_start + offset + 1
                offset = 0  # Reset comparison offset
              
                # Ensure right_start is always ahead of left_start
                if left_start >= right_start:
                    right_start = left_start + 1
                  
            # Case 3: Right substring is smaller at current offset
            else:
                # Skip the entire right substring and its compared portion
                right_start = right_start + offset + 1
                offset = 0  # Reset comparison offset
      
        # Return the suffix starting from the optimal position
        return s[left_start:]