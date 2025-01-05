"""
Platform: LeetCode
Problem: 3280 - Convert Date to Binary
Difficulty: Easy
URL: https://leetcode.com/problems/convert-date-to-binary/

Date: 2025-01-01
Time: 11:28

Author: Kyire

Algorithm: Math
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 0 ms
Memory: 17.54 MB
"""


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def convertToBinary(num):
            binary = ""
            while num > 0:
                binary = str(num % 2) + binary
                num //= 2
            return binary

        year, month, day = date[:4], date[5:7], date[8:]

        year = convertToBinary(int(year))
        month = convertToBinary(int(month))
        day = convertToBinary(int(day))

        return year + "-" + month + "-" + day
