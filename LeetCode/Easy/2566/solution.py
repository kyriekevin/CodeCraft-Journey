class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        maxv = num

        for ch in s:
            if ch != '9':
                maxv = int(s.replace(ch, '9'))
                break

        minv = int(s.replace(s[0], '0'))

        return maxv - minv
