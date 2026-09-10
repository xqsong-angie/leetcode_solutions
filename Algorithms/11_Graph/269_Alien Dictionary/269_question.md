269. Alien Dictionary

https://www.lintcode.com/problem/892/

Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

You may assume all letters are in lowercase
At first different letter, if the letter in s precedes the letter in t in the given list order, then the dictionary order of s is less than t
The dictionary is invalid, if string a is prefix of string b and b is appear before a
If the order is invalid, return an empty string
There may be multiple valid order of letters, return the smallest in normal lexicographical order
The letters in one string are of the same rank by default and are sorted in Human dictionary order
Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"