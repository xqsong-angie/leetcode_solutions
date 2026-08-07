#20260806
class Solution:#hash+backtracking
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        """
        Check if string s follows the given pattern where each character in pattern
        can map to a substring in s (bijective mapping).

        Args:
            pattern: Pattern string containing characters
            s: Target string to match against the pattern

        Returns:
            True if s follows the pattern, False otherwise
        """

        def backtrack(pattern_idx: int, string_idx: int) -> bool:
            """
            Recursively try to match pattern with string using backtracking.

            Args:
                pattern_idx: Current index in the pattern
                string_idx: Current index in the string s

            Returns:
                True if valid matching found, False otherwise
            """
            # Base case: both pattern and string are fully processed
            if pattern_idx == pattern_length and string_idx == string_length:
                return True

            # Invalid case: one is exhausted but not the other, or insufficient characters left
            if (pattern_idx == pattern_length or
                string_idx == string_length or
                string_length - string_idx < pattern_length - pattern_idx):
                return False

            current_pattern_char = pattern[pattern_idx]

            # Try all possible substrings starting from current position in s
            for end_idx in range(string_idx, string_length):
                substring = s[string_idx:end_idx + 1]

                # Case 1: Current pattern character already has a mapping
                if pattern_to_string.get(current_pattern_char) == substring:
                    if backtrack(pattern_idx + 1, end_idx + 1):
                        return True

                # Case 2: Current pattern character has no mapping yet and substring is not used
                elif current_pattern_char not in pattern_to_string and substring not in used_substrings:
                    # Create new mapping
                    pattern_to_string[current_pattern_char] = substring
                    used_substrings.add(substring)

                    # Recursively check if this mapping works
                    if backtrack(pattern_idx + 1, end_idx + 1):
                        return True

                    # Backtrack: remove the mapping if it doesn't lead to solution
                    del pattern_to_string[current_pattern_char]
                    used_substrings.remove(substring)

            return False

        # Initialize variables
        pattern_length = len(pattern)
        string_length = len(s)
        pattern_to_string = {}  # Maps pattern characters to substrings
        used_substrings = set()  # Tracks which substrings are already mapped

        # Start backtracking from the beginning
        return backtrack(0, 0)
