class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        res = sum((k + v) // (k + 1) * (k + 1) for k, v in cnt.items())
        return res
