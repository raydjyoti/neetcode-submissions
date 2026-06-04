class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # [10, 6, 9, 3]
        # + = 9, 3 = 12 = [10, 6, 12]
        # [10, 6, 12, -11]
        # * = 12 * -11 = -132 = [10, 6, -132]
        # / = 6 / -132 = 0 = [10, 0]
        # * = 10 * 0 = 0 = [0]
        # [0, 17]
        # + = 17 + 0 = [17]
        # [17, 5]
        # + = 17 + 5 = 22

        stack = []
        def isNum(n):
            try:
                num = int(n)
                return True
            except:
                return False


        def calRes(op, first, second):
            if (op == "+"): return first + second
            elif (op == "-"): return first-second
            elif (op == "*"): return first*second
            elif (op == "/"): return int(first/second)

        for s in tokens:
            if (isNum(s)): stack.append(s)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                res = calRes(s,first,second)
                stack.append(res)

        return int(stack[0])