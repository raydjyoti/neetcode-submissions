class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)

        for i in range(len(temperatures)):
            num = temperatures[i]

            if (len(stack) == 0):
                stack.append([num, i])
                continue

            while (len(stack) and num > stack[-1][0]):
                n = stack.pop()
                index = n[1]
                diff = i - index
                output[index] = diff

            stack.append([num, i])

        return output