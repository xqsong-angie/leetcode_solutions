You are moderating a newspaper page, and you have to align the text on the page properly. The text is provided to you in the following format:

paragraphs is an array of paragraphs, where each paragraph is represented as an array of words;

aligns is an array representing the alignment of each paragraph from paragraphs - each element is either "LEFT" or "RIGHT";

width represents the maximum number of characters each line of the output can include.

Your task is to produce a newspaper page according to the following specifications:

For each paragraph paragraphs[i], include all the words paragraphs[i][j] in order, separated by spaces;  

Include as many words as possible per each page line (the length of the line must be less than or equal to width), and put the next word on a new line if it would exceed the limit;  

In the case of excess whitespace, words from paragraphs[i] should be aligned according to aligns[i] - if aligns[i] = "LEFT", the line should have trailing spaces, if aligns[i] = "RIGHT", it should have leading spaces;  

Include a border of * characters around all the edges of the result - these characters don't count toward the width, they are just added to make output more pretty.  

It is guaranteed that it is possible to justify the given paragraphs to the newspaper. Return the resulting newspaper page as an array of strings.  

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(paragraph.length * paragraph[0].length * width) will fit within the execution time limit.