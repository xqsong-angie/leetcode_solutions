7. TikTok Circular Clip Analysis

The TikTok team is analyzing clips to measure their unique content strength. Given a string clip of length n consisting of only lowercase English characters, imagine the clip is circular, meaning after the n-th character, the sequence continues from the 1st character again.

Circular Nature: Since the clip is circular, you can form substrings that wrap around from the end of the string back to the beginning. For instance, with the string "yxz", valid substrings include "y", "x", "z", "yx", "xz", "zy", "yxz", "xzy" and "zyx".

The "content strength" of a circular clip is determined by the number of unique substrings that consist of only consonants. Your task is to find the content strength of this circular clip.


Example

Input:
clip = "bac"

Output:
3

Explanation:
The different possible substrings of the circular clip are: ["b", "a", "c", "ba", "ac", "cb", "bac", "acb", "cba"].
The substrings that consist of only consonants are: ["b", "c", "cb"].