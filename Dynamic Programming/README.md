## Longest Common Subsequence (LCS)

Given two strings, S1 and S2, the task is to find the length of the Longest Common Subsequence. If there is no common subsequence, return 0. A subsequence is a string generated from the original string by deleting 0 or more characters and without changing the relative order of the remaining characters. For example , subsequences of “ABC” are “”, “A”, “B”, “C”, “AB”, “AC”, “BC” and “ABC”. In general a string of length n has 2n subsequences.

LCS problem has great applications like diff utility (find the difference between two files) that we use in our day to day software development.

**Examples:**

```
Input: S1 = “ABC”, S2 = “ACD”

Output: 2

Explanation: The longest subsequence which is present in both strings is “AC”.
```

Approach Used: Using Recursion – O(2^min(m,n)) Time and O(min(m, n)) Space

```
The idea is to compare the last two characters. While comparing the strings S1 and S2 two cases arise:


1. Match : Make the recursion call  for the remaining strings (strings of lengths m-1 and n-1) and add 1 to result.

2. Do not Match : Make two recursive calls. First for lengths m-1 and n, and second for m and n-1. Take the maximum of two results.
 
Base case : If any of the strings become empty, we return 0.
```
