"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        newsum = (int(a, 2) + int(b, 2))
        return bin(newsum)[2:]

"""
Results

Runtime: Beats 100%
Memory: Beats 27.59

Run is good, how to improve memory usage?
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

"""
Results

Runtime: Beats 45.8%
Memory: Beats 39.1%

Weird
"""
