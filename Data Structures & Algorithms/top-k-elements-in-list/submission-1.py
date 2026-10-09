class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(list)
        for n in nums:
            if n in counter:
                v = counter[n][1] + 1
                counter[n] = [n, v]
            else:
                counter[n] = [n, 1]
            
        res = sorted(counter.values(), key=lambda x: x[1], reverse=True)
        return [r[0] for r in res[:k]]
