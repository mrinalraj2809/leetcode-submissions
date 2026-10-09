class Solution:
    def isInteger(self, token):
        try:
            value = int(token)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                res.append(int(token))
                continue

            b = res.pop()
            a = res.pop()

            if token == "+":
                res.append(a + b)
            elif token == "-":
                res.append(a - b)
            elif token == "*":
                res.append(a * b)
            else:
                # RPN division must truncate toward zero
                res.append(int(a / b))

        return res[0]
        # res = []
        # for c in tokens:
        #     print(c)
        #     print(len(c))
        #     if self.isInteger(c): 
        #         res.append(int(c))
        #     else:
        #         maxVal = -999
        #         # print(res)
        #         counter = 0
        #         while len(res)!=0 and counter <2:
        #             print(res)
        #             val = res.pop()
        #             if c == '+':
        #                 maxVal = val if maxVal == -999 else maxVal + val
        #             elif c == '-':
        #                 maxVal = val if maxVal == -999 else val - maxVal
        #             elif c == '*':
        #                 maxVal = val if maxVal == -999 else maxVal * val
        #             elif c == '/':
        #                 maxVal = val if maxVal == -999 else val / maxVal
        #             counter = counter + 1
        #         res.append(maxVal)
        # return int(res.pop())