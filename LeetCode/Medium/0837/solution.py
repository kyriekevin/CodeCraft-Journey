class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0

        f = [0.0] * (k + maxPts)
        for i in range(k, min(n, k + maxPts - 1) + 1):
            f[i] = 1.0

        f[k - 1] = float(min(n - k + 1, maxPts)) / maxPts
        for i in range(k - 2, -1, -1):
            f[i] = f[i + 1] - (f[i + maxPts + 1] - f[i + 1]) / maxPts
        return f[0]
