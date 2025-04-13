from collections import defaultdict
import math

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        rk = defaultdict(int)
        h = [0] + [int(x) for x in input().split()]
        a = [0] + [int(x) for x in input().split()]
        t = [0] + [int(x) for x in input().split()]
        for i in range(1, n + 1):
            rk[t[i] + 1] = i

        l, r = 0, float("inf")
        for i in range(1, n):
            A = h[rk[i]] - h[rk[i + 1]]
            B = a[rk[i + 1]] - a[rk[i]]
            if B > 0:
                r = min(r, math.ceil(A / B) - 1)
            elif B < 0:
                l = max(l, math.floor(A / B) + 1)
            elif A <= 0:
                r = -1
                break

        if l > r:
            l = -1
        print(l)
