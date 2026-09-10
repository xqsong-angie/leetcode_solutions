#20260805 🔥括号只考虑无限循环
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle zero numerator case
        if numerator == 0:
            return "0"
      
        result = []
      
        # Determine if result should be negative
        # XOR returns True if signs are different
        is_negative = (numerator > 0) ^ (denominator > 0)
        if is_negative:
            result.append("-")
      
        # Work with absolute values to simplify calculation
        dividend, divisor = abs(numerator), abs(denominator)
      
        # Add the integer part
        result.append(str(dividend // divisor))
      
        # Calculate remainder
        remainder = dividend % divisor
      
        # If no remainder, return the integer result
        if remainder == 0:
            return "".join(result)
      
        # Add decimal point for fractional part
        result.append(".")
      
        # Dictionary to track remainders and their positions
        # Used to detect repeating decimals
        remainder_positions = {}
      
        # Process the fractional part
        while remainder:
            # Store current remainder's position in result
            remainder_positions[remainder] = len(result)
          
            # Perform long division: multiply remainder by 10
            remainder *= 10
          
            # Add the next digit to result
            result.append(str(remainder // divisor))
          
            # Calculate new remainder
            remainder = remainder % divisor
          
            # Check if we've seen this remainder before (repeating pattern)
            if remainder in remainder_positions: #🔥判断的是余数，不是输出的数字
                # Insert opening parenthesis at the start of repeating sequence
                result.insert(remainder_positions[remainder], "(")
                # Add closing parenthesis at the end
                result.append(")")
                break
      
        return "".join(result)
