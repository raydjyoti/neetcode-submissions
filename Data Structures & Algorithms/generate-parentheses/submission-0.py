class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def bc(op, close, s):

            if (op < n):
                newS = s+"("
                bc(op+1, close, newS)

            if (close < op):
                newS = s+")"
                bc(op, close+1, newS)

            if (op == close and op == n):
                output.append(s)

            return

        bc(0, 0, "")
        return output