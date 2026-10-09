class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = []
        for i in range(len(position)):
            d = target - position[i]
            res.append(d/speed[i])
        
        fleet=0
        if len(res)==1:
            fleet = 1
            return fleet
        list_tup_res = [[p, r] for p, r in zip(position, res)]
        
        list_tup_res.sort(key= lambda x: x[0])
        stack_max = []
        for t in range(len(list_tup_res)-1, -1, -1):
            if len(stack_max) == 0:
                stack_max.append(list_tup_res[t][1])
            else:
                maxim = stack_max[-1]
                if list_tup_res[t][1] >  maxim:
                    stack_max.append(list_tup_res[t][1])
        # print(list_tup_res)
        # print(stack_max)
        return len(stack_max)