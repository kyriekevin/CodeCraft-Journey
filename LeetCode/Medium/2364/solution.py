class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        for i, x in enumerate(nums):
            res += i - mp[x - i]
            mp[x - i] += 1
        return res
