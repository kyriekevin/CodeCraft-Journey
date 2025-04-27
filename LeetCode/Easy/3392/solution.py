class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1, n - 1):
            left, right = i - 1, i + 1
            if 2 * (nums[left] + nums[right]) == nums[i]:
                res += 1
        return res
