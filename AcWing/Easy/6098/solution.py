"""
Platform: AcWing
Problem: 6098 - 局部最小值
Difficulty: Easy
URL: https://www.acwing.com/problem/content/6101/

Date: 2025-02-15
Time: 16:0

Author: Kyire
"""

n, l, r = map(int, input().split())

arr = list(map(int, input().split()))
res = min(arr[l - 1 : r])
print(res)
