A virtual memory management system in an operating system uses Least Recently Used (LRU) cache. When a requested memory page is not in the cache and the cache is full, the page that was least recently used should be removed from the cache to make room for the requested page. If the cache is not full, then the requested page is added to the cache and considered to be the most recently used element in the cache. A given page should occur once in the cache at most.

Given the maximum size of the cache and an array of page requests, calculate the number of cache misses. A cache miss occurs when a page is requested but is not found in the cache.

Input
The first line of the input consists of a positive integer- inputNum_size, representing the total number of pages(N).
The second line consists of N space-separated positive integers representing the page requests for N pages.
The last line consists of an positive integer- size, representing the size of the cache.

Output
Print an integer representing the number of cache misses.

Note
The cache is initially empty and the list contains pages numbered in the range 1-50. A page at index i in the list is requested before a page at index i+1.

Example
Input:
6
1 2 1 3 1 2
2

Output:
5

Explanation:
Cache state as requests come in ordered longest-time-in-cache to shortest-time-in-cache:
1 *
1 2 *
1 2
2 3 *
3 1 *
1 2 *