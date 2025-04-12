N = int(4e5 + 10)
a, s = [0] * N, [0] * N

def solve():
    global a, s
    n, m = map(int, input().split())
    arr = [int(x) % m for x in input().split()]
    arr = sorted(arr)

    for i in range(1, n + 1):
        a[i] = arr[i - 1]
    for i in range(1, n + 1):
        a[i + n] = a[i] + m

    for i in range(1, 2 * n + 1):
        s[i] = s[i - 1] + a[i]

    res = float('inf')
    for i in range(1, n + 1):
        l, r = i, i + n - 1
        mid = (l + r) // 2
        left = (mid - l + 1) * a[mid] - (s[mid] - s[l - 1])
        right = s[r] - s[mid] - (r - mid) * a[mid]
        res = min(res, left + right)
    print(res)

T = int(input())
for _ in range(T):
    solve()
