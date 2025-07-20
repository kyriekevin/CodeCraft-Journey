class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        for i in range(len(folder)):
            folder[i] = folder[i] + '/'

        res = []
        for i in range(len(folder)):
            if i == 0 or len(res[-1]) > len(folder[i]) or folder[i][:len(res[-1])] != res[-1]:
                res.append(folder[i])

        for i in range(len(res)):
            res[i] = res[i][:-1]

        return res
