7. Maximum Positive Feedback

The TikTok Content creator's videos receives feedback from viewers over time, represented as a binary string, videoFeedback:

- 1 indicates positive reactions (likes, shares, or comments).
- 0 indicates negative reactions (skips or dislikes).

The creator wants to improve a video's overall positive reception by strategically targeting a portion of the video from re-editing or improvement. Here's the strategy:

- Choose one specific segment of the video (interval [i, j]) to leave unchanged, where i > 0 and j < videoFeedback_size.
- Outside this segment, the plan is to completely change the content—flipping negative reactions to positive (0 to 1) and positive reactions to negative (1 to 0).

The objective is to maximize the total positive feedback (1s) for the entire video after performing this operation.

Note: The operation must be performed only once.


Example

Given videoFeedback_size = 6 and videoFeedback = "100110",
The interval i = 4 to j = 5 can be selected as the unchanged segment of the video.
Flipping the bits from index 1 to 3 transforms the string from "100110" to "011110".
Next, flipping the bit at index 6 (i.e., the last bit) changes the string from "011110" to "011111".
As this string contains 5 ones, the output should be 5. There are no intervals that produce an output greater than 5.


Function Description

Complete the function getMaxPositiveFeedback in the editor below.

getMaxPositiveFeedback has the following parameter:
  string videoFeedback: a binary string representing the feedback on a video, where 1 represents positive feedback and 0 represents negative reaction

Returns
  int: the maximum positive feedback after an operation


Constraints

- 2 <= videoFeedback_size <= 3 * 10^5
- videoFeedback[i] = '0' or '1'


Input Format For Custom Testing

The first line contains string videoFeedback.


Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
10000011  ->  videoFeedback = "10000011"

Sample Output
6

Explanation
Given videoFeedback_size = 8 and videoFeedback = "10000011", we can select i = 7 and j = 7.
First, flip the bits from index 1 to 6. The videoFeedback becomes "01111111".
Next, flip the bit at index 8. The videoFeedback becomes "01111110".
Hence, the answer is 6. It can be proven that the answer cannot be greater than 6.


Sample Case 1

Sample Input For Custom Testing

STDIN        FUNCTION
-----        --------
0100101  ->  videoFeedback = "0100101"

Sample Output
5

Explanation
Given videoFeedback_size = 7 and videoFeedback = "0100101", we can select i = 2 and j = 2.
First, flip the bit at index 1. The feedback becomes "1100101".
Next, flip the bits from index 3 to 7. The feedback becomes "1111010".
Hence, the answer is 5. It can be proven that the answer cannot be greater than 5.