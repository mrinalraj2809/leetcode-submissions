class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False 
        return False if sorted(s) != sorted(t) else True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        # res = []
        # # strs.sort()
        # for i in range(len(strs)):
        #     flag = False
        #     for j in range(len(res)):
        #         if self.isAnagram(strs[i], res[j][0]):
        #             res[j].append(strs[i])
        #             flag = True
        #             break
        #     if not flag:
        #         res.append([strs[i]])
        # return res


