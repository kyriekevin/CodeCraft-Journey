"""
Platform: Codeforces
Problem: 1352C - K-th Not Divisible by n
Rating: 1200
URL: https://codeforces.com/problemset/problem/1352/C
Tags: binary search, math

Date: 2025-03-16
Time: 11:38

Author: Kyire

"""


def solve(n, k):
    if k % (n - 1) == 0:
        q = k // (n - 1) - 1
        r = n - 1
    else:
        q = k // (n - 1)
        r = k % (n - 1)

    return q * n + r


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
