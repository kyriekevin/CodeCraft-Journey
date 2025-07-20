class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        idx = sorted(range(len(nums)), key=lambda i: nums[i])
        idx = sorted(idx[-k:])
        return [nums[i] for i in idx]
