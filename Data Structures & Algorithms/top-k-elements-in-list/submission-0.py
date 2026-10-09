from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myc = Counter(nums)
        tup = myc.most_common(k)
        res = []
        for i in range(k):
            res.append(tup[i][0])
        return res