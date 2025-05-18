class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two = 0, len(nums) - 1

        for i in range(two + 1):
            while nums[i] == 2 and i < two:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

        return nums
