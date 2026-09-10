#20260807
#https://algo.monster/liteproblems/65
class Solution:
    def isNumber(self, s: str) -> bool:
        """
        Validates if a string represents a valid number.
        Valid numbers include integers, decimals, and scientific notation.
      
        Args:
            s: Input string to validate
          
        Returns:
            bool: True if string is a valid number, False otherwise
        """
        n = len(s)
        index = 0
      
        # Check for optional sign at the beginning
        if s[index] in '+-':
            index += 1
      
        # String cannot be just a sign
        if index == n:
            return False
      
        # Check for invalid cases: lone decimal point or decimal point followed by e/E
        if s[index] == '.' and (index + 1 == n or s[index + 1] in 'eE'):
            return False
      
        # Initialize flags for decimal point and exponent
        has_decimal = 0
        has_exponent = 0
        current_index = index
      
        # Parse the rest of the string
        while current_index < n:
            if s[current_index] == '.':
                # Decimal point cannot appear after exponent or if already present
                if has_exponent or has_decimal:
                    return False
                has_decimal += 1
              
            elif s[current_index] in 'eE':
                # Check for invalid exponent placement
                # Cannot have multiple exponents, at the start, or at the end
                if has_exponent or current_index == index or current_index == n - 1:
                    return False
                has_exponent += 1
              
                # Check for optional sign after exponent
                if s[current_index + 1] in '+-':
                    current_index += 1
                    # Sign cannot be the last character
                    if current_index == n - 1:
                        return False
                      
            elif not s[current_index].isnumeric():
                # Any non-numeric character (except . and e/E) is invalid
                return False
              
            current_index += 1
          
        return True
#感觉这道题这个解法比较稀碎，应该还有更好的解法