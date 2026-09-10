#20260803
from collections import Counter
#https://algo.monster/liteproblems/409
class Solution:
    def longestPalindrome(self, s: str) -> int:#🔥built with those letters注意是用这些字符组成的序列，不是原序列
        # Count frequency of each character in the string
        char_count = Counter(s)
      
        # Calculate the length of the longest palindrome
        # For each character, we can use pairs (even count) in the palindrome
        palindrome_length = sum(count // 2 * 2 for count in char_count.values())
      
        # If palindrome length is less than string length, we can add one odd character in the middle
        # This checks if there's at least one character with odd frequency
        if palindrome_length < len(s):
            palindrome_length += 1
      
        return palindrome_length