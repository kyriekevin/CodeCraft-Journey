class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans = [], []
        cnt = 0

        for num in nums:
            if num > 0:
                cnt = 0
                seen.insert(0, num)
            else:
                cnt += 1
                if cnt <= len(seen):
                    ans.append(seen[cnt - 1])
                else:
                    ans.append(num)

        return ans
