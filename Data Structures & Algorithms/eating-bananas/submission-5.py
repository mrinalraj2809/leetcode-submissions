class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            k = (l + r) // 2 # notice l = 0 and r = upperbound of piles i.e no need to sort piles as we change k i.e. the eating rate between this range.

            eating_time = sum(math.ceil(pile / k) for pile in piles) # if k decreases , eating time increases

            if eating_time <= h:
                r = k
            else:
                l = k + 1

        return r
        # piles.sort()
        # maxim_k = piles[-1]
        # k = piles[-1]
        # l = 0
        # r = len(piles) - 1
        # while l < r :
        #     possible_k = piles[r]
        #     # max_rate_per_piles = math.floor(h/len(piles))
        #     eating_time = int(math.ceil(maxim_k/possible_k)) * len(piles)
        #     if eating_time > h:
        #         break
        #     elif eating_time <= h:
        #         k = possible_k
        #         r -= 1
        #     # k = min(k, int(math.ceil(maxim_k/possible_k)))
        # eating_time = 0
        # while eating_time <= h :
        #     eating_time = int(math.ceil(maxim_k / k)) * len(piles)
        #     k -= 1
        # return k
