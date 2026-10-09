class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # lets have a stack
        # Current element is greater than top, we pop and update the index distance simulateneouly
        # Once current becomes smaller we break and copy other index as it is
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, 0, -1):
            curr = i
            for j in range(i-1, -1, -1):
                if temperatures[curr] > temperatures[j]:
                    res[j] = curr - j 
                else:
                    break
        return res
        # result = [0] * len(temperatures) 
        # for i in range(len(temperatures)):
        #     counter = 0
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] <= temperatures[i]:
        #             counter += 1
        #         else:
        #             break
        #     if j == len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
        #             counter = 0
        #     result[i] = counter

        # return result