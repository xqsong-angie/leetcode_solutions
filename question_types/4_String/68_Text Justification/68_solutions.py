#20260807
#https://algo.monster/liteproblems/68
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Formats text with full justification where each line has exactly maxWidth characters.
      
        Args:
            words: List of words to be justified
            maxWidth: Maximum width of each line
          
        Returns:
            List of fully justified text lines
        """
        result = []
        word_index = 0
        total_words = len(words)
      
        # Process words until all are placed in lines
        while word_index < total_words:
            # Collect words that fit in the current line
            current_line_words = []
            current_line_length = len(words[word_index])
            current_line_words.append(words[word_index])
            word_index += 1
          
            # Keep adding words while they fit (accounting for minimum one space between words)
            while word_index < total_words and current_line_length + 1 + len(words[word_index]) <= maxWidth:
                current_line_length += 1 + len(words[word_index])
                current_line_words.append(words[word_index])
                word_index += 1
          
            # Handle last line or single-word line (left-justified)
            if word_index == total_words or len(current_line_words) == 1:
                # Join words with single spaces and pad right with spaces
                left_justified = ' '.join(current_line_words)
                right_padding = ' ' * (maxWidth - len(left_justified))
                result.append(left_justified + right_padding)
                continue
          
            # Calculate space distribution for full justification
            # Total spaces needed = maxWidth - sum of word lengths
            total_spaces = maxWidth - (current_line_length - len(current_line_words) + 1)
          
            # Distribute spaces evenly between words
            gaps_between_words = len(current_line_words) - 1
            base_spaces_per_gap, extra_spaces = divmod(total_spaces, gaps_between_words)
          
            # Build the justified line
            justified_line = []
            for word_position, word in enumerate(current_line_words[:-1]):
                justified_line.append(word)
                # Add base spaces plus one extra space for the first 'extra_spaces' gaps
                spaces_to_add = base_spaces_per_gap + (1 if word_position < extra_spaces else 0)
                justified_line.append(' ' * spaces_to_add)
          
            # Add the last word (no spaces after it)
            justified_line.append(current_line_words[-1])
            result.append(''.join(justified_line))
          
        return result