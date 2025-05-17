class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0

        for j, x in enumerate(nums):
            l, r = 0, j
            while l < r:
                mid = l + r >> 1
                if nums[mid] > upper - x:
                    r = mid
                else:
                    l = mid + 1
            right = l

            l, r = 0, j
            while l < r:
                mid = l + r >> 1
                if nums[mid] >= lower - x:
                    r = mid
                else:
                    l = mid + 1
            left = l

            res += right - left
        return res
